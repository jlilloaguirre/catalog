# Catalog API

A production-ready REST API for managing a catalog of books, developed with Django REST Framework and deployed through a complete DevOps pipeline using Docker, Kubernetes, Helm, GitHub Actions, Semantic Release and Argo CD.

The project demonstrates both backend API development and an automated GitOps deployment workflow, from writing code to releasing and deploying a new application version.

---

# Features

## Book management

The API supports full CRUD operations:

- Create a book
- List all books
- Retrieve a single book
- Update an existing book
- Delete a book

Each book contains:

- ID
- Title
- Description
- Author
- ISBN
- Published date
- Creation timestamp

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/` | Health check |
| GET | `/api/books/` | List all books |
| POST | `/api/books/` | Create a new book |
| GET | `/api/books/<id>/` | Retrieve one book |
| PUT | `/api/books/<id>/` | Update a book |
| DELETE | `/api/books/<id>/` | Delete a book |

---

# Example Requests

## Create a book

```bash
curl -X POST http://localhost:8081/api/books/ \
-H "Content-Type: application/json" \
-d '{
    "title":"Designing Data-Intensive Applications",
    "description":"Modern distributed systems",
    "author":"Martin Kleppmann",
    "isbn":"9781449373320",
    "published_date":"2017-03-16"
}'
```

---

## Retrieve all books

```bash
curl http://localhost:8081/api/books/
```

---

## Retrieve one book

```bash
curl http://localhost:8081/api/books/1/
```

---

## Update a book

```bash
curl -X PUT http://localhost:8081/api/books/1/ \
-H "Content-Type: application/json" \
-d '{
    "title":"Updated title",
    "description":"Updated description",
    "author":"Updated author",
    "isbn":"9781449373320",
    "published_date":"2017-03-16"
}'
```

---

## Delete a book

```bash
curl -X DELETE http://localhost:8081/api/books/1/
```

---

# Technology Stack

## Backend

- Python
- Django
- Django REST Framework
- PostgreSQL

## DevOps

- Docker
- Docker Compose
- Kubernetes (k3d)
- Helm
- Argo CD
- GitHub Actions
- Semantic Release
- GitHub Container Registry (GHCR)

---

# Local Development

## Clone the repository

```bash
git clone https://github.com/jlilloaguirre/catalog.git
cd catalog
```

---

## Create the virtual environment

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Apply database migrations

```bash
python manage.py migrate
```

---

## Run the development server

```bash
python manage.py runserver
```

Application:

```
http://127.0.0.1:8000
```

Admin:

```
http://127.0.0.1:8000/admin
```

---

## Create an administrator

```bash
python manage.py createsuperuser
```

---

# Testing

Run the automated tests

```bash
pytest
```

Run Django system checks

```bash
python manage.py check
```

Verify database migrations

```bash
python manage.py makemigrations --check
```

---

# Docker

Build the application image

```bash
docker build -t ghcr.io/jlilloaguirre/catalog:test .
```

Run locally

```bash
docker compose up --build
```

---

# Kubernetes

Validate the Helm chart

```bash
helm lint ./books-catalog-chart
```

Deploy manually

```bash
helm install book-catalog-api ./books-catalog-chart
```

Inspect the deployment

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

# CI/CD Pipeline

Every push to the **main** branch automatically triggers the GitHub Actions workflow.

The pipeline performs the following steps:

1. Install project dependencies.
2. Execute the automated test suite.
3. Validate the Django project.
4. Generate a Semantic Release version.
5. Build a Docker image.
6. Push the image to GitHub Container Registry.
7. Update the production Helm values.
8. Commit the new image version automatically.
9. Argo CD detects the Git change.
10. Kubernetes deploys the new application version automatically.

This provides a complete GitOps deployment workflow with minimal manual intervention.

---

# Production Deployment

The deployed application is available through Kubernetes.

API

```
http://localhost:8081/api/books/
```

Argo CD

```
http://localhost:8081/argocd
```

---

# Production Improvements

To support a production-style deployment, the application includes:

- Gunicorn as the WSGI application server
- WhiteNoise for static file serving
- Helm-managed Kubernetes manifests
- Traefik Ingress routing
- PostgreSQL persistent database
- Automatic static asset collection during container startup
- Automated image versioning with Semantic Release
- Continuous deployment using Argo CD

---

# Repository Structure

```
catalog/
│
├── api/                     # Django REST API
├── bookcatalog/             # Django project configuration
├── books-catalog-chart/     # Helm chart
├── envs/                    # Deployment values
├── .github/workflows/       # GitHub Actions
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── README.md
```

---

# Future Improvements

Potential extensions include:

- Authentication and authorization
- Search and filtering
- Pagination
- Swagger / OpenAPI documentation
- Partial updates (PATCH)
- Book cover image uploads
- Rate limiting
- Logging and monitoring
- Caching with Redis

---

# Author

**Joan Lillo Aguirre**

Diploma in DevOps (Summer 2026)

CCT College Dublin