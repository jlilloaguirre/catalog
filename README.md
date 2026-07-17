## Local setup

Activate the virtual environment:

```bash
source ./.venv/bin/activate
```

Run the development server:

```bash
python manage.py runserver
```

The app will be available at:

```text
http://127.0.0.1:8000/
```

The admin site will be available at:

```text
http://127.0.0.1:8000/admin/
```

Create an admin user:

```bash
python manage.py createsuperuser
```