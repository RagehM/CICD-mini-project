import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from app.main import app
from app import models
from app.database import engine
import redis.asyncio as redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@pytest.fixture
def client():
    """Create a test client."""
    
    models.Base.metadata.create_all(bind=engine)
    yield TestClient(app)

    models.Base.metadata.drop_all(bind=engine)

@pytest_asyncio.fixture(autouse=True)
async def setup_test_cache():
    """Initialize test cache for each test."""
    test_redis = await redis.from_url("redis://localhost:6379", decode_responses=True)
    FastAPICache.init(RedisBackend(test_redis), prefix="fastapi-cache-test")
    yield
    await test_redis.aclose()


def test_create_student(client):
    """Test creating a new student."""
    response = client.post(
        "/students/",
        json={"name": "John", "university": "MIT", "age": 22}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["university"] == "MIT"
    assert data["age"] == 22

def test_get_students(client):
    """Test getting all students, including testing the cache."""
    # First create a student
    client.post("/students/", json={"name": "Test", "university": "Harvard", "age": 20})
    
    response1 = client.get("/students/")
    assert response1.status_code == 200
    data1 = response1.json()
    assert isinstance(data1, list)
    assert len(data1) > 0
    
    response2 = client.get("/students/")
    assert response2.status_code == 200
    data2 = response2.json()
    
    assert data1 == data2

def test_get_nonexistent_student(client):
    """Test getting a non-existent student."""
    response = client.get("/students/99999")
    assert response.status_code == 404
