# Django Authentication Setup - Summary & Key Points

This is a comprehensive guide on setting up authentication in Django. Here's a structured overview:

## Core Concepts

**Authentication** verifies user identity and controls access to your web application. Django's built-in framework provides:

- User account management
- Secure login/logout/registration
- View protection with decorators
- Permission and role management

## Setup Process

### 1. Virtual Environment

```bash
python -m venv myenv
.\\myenv\\Scripts\\activate
pip install django

```

### 2. Project Structure

```bash
django-admin startproject myproject
python manage.py startapp myapp

```

### 3. Custom User Model

Extend `AbstractUser` to add custom fields:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    User_Type = models.CharField(choices=USER, max_length=100, null=True)

```

**Important:** Set in `settings.py`:

```python
AUTH_USER_MODEL = "myapp.CustomUser"

```

### 4. Database Setup

```bash
python manage.py makemigrations myapp
python manage.py migrate
python manage.py createsuperuser

```

## Key Features Implemented

### Signup View

- Validates password matching
- Creates new user with `create_user()`
- Redirects to login on success

### Login View

- Uses `authenticate()` to verify credentials
- Calls `login()` to create session
- Redirects to home page

### Logout View

- Uses `logout()` to end session
- Redirects to login page

### Protected Views

Use `@login_required` decorator:

```python
@login_required
def departmentpage(req):
    # Only accessible to logged-in users

```

## Security Best Practices

✅ Always use `{% csrf_token %}` in forms

✅ Use `method="POST"` for sensitive data

✅ Validate username existence before creation

✅ Compare passwords before saving

✅ Use Django's built-in `create_user()` (hashes passwords automatically)

## Common Issues to Watch

- Remove `__pycache__`, `db.sqlite3`, and migration files before initial migrations
- Set `LOGIN_URL` in  for `@login_required` redirects
- Include templates directory in `TEMPLATES['DIRS']`

This setup provides a solid foundation for user authentication in Django projects! 🔐