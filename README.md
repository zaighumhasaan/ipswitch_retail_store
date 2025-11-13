# Ipswich Retail E-commerce Application

A modern e-commerce platform built with Django, demonstrating DevOps practices including CI/CD, containerization, automated testing, and cloud deployment.

## Features

- Product catalog with categories
- Shopping cart functionality
- User authentication and order management
- Responsive Bootstrap 5 design
- Admin dashboard for product and order management

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: PostgreSQL (SQLite for development)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: Railway
- **Testing**: Django TestCase, Coverage.py

## Local Development Setup

### Prerequisites

- Python 3.11+
- PostgreSQL (optional for local dev)
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ip-switch
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000 to view the application.

## Docker Setup

Build and run with Docker:

```bash
docker-compose up --build
```

## Running Tests

Run all tests:
```bash
python manage.py test
```

With coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Deployment

The application is automatically deployed to Railway when changes are pushed to the main branch.

### Environment Variables (Production)

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False
- `ALLOWED_HOSTS`: Your domain name
- `DATABASE_URL`: PostgreSQL connection string (auto-set by Railway)

## Project Structure

```
ip-switch/
├── ipswich_retail/     # Django project settings
├── store/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── urls.py         # URL routing
│   └── templates/      # HTML templates
├── static/             # Static files (CSS, JS, images)
├── templates/          # Global templates
├── docs/               # Documentation
├── planning/           # Architecture and wireframes
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── .github/workflows/  # CI/CD pipelines
```

## Admin Access

Access the admin panel at `/admin` with your superuser credentials.

## License

This project is created for educational purposes as part of a DevOps assessment.
