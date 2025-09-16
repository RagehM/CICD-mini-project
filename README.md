# FastAPI Student Management System

A simple REST API built with FastAPI for managing student records with Redis caching.

## Features

- CRUD operations for student records
- Redis caching for improved performance
- FastAPI for modern, fast API development
- SQLite database backend
- Automated testing with pytest

## Prerequisites

- Python 3.12
- Redis
- Docker and Docker Compose (optional)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/RagehM/CICD-mini-project.git
cd CICD-mini-project
```

2. Create and activate virtual environment:

```sh
python -m venv CICD_mini_project_env
source CICD_mini_project_env/Scripts/activate  # Windows
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

4. Start Redis using Docker:

```sh
docker-compose up -d redis
```

## Running the Application

1. Start the FastAPI server:

```sh
uvicorn app.main:app --reload
```

2. Access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `POST /students/` - Create a new student
- `GET /students/` - List all students (cached)
- `GET /students/{student_id}` - Get a specific student
- `DELETE /students/{student_id}` - Delete a student

## Running Tests

Run tests using pytest:

```sh
pytest tests/ -v
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database configuration
│   └── create_db.py     # Database initialization
├── tests/
│   └── test_main.py     # API tests
├── docker-compose.yml   # Docker services config
├── requirements.txt     # Python dependencies
└── README.md
```

## CI/CD Pipeline

The project includes GitHub Actions workflows for:

- Running automated tests on push
- Ensuring code quality
- Testing with Redis integration

## Environment Variables

- `REDIS_URL`: Redis connection URL (default: "redis://localhost:6379")

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
