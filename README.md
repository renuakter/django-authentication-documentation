# django-authentication-documentation
# Django Authentication Setup - Complete Guide

## Introduction

**Authentication** verifies user identity in web applications, ensuring only authorized users can access certain features. Django's authentication framework provides:

- User account creation and management
- Secure login, logout, and registration
- View access restriction using decorators (`@login_required`)
- Permission and role management via admin panel

---

## Step-by-Step Setup

### 1. Virtual Environment Setup

A virtual environment isolates your project's dependencies from other Python projects.

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
.\\myenv\\Scripts\\activate

# Deactivate when done
.\\myenv\\Scripts\\deactivate

```

### 2. Install Django

```bash
pip install django

```

### 3. Create Project and App

**Project**: The overall website containing settings, URLs, and configuration.

```bash
django-admin startproject myproject

```

**App**: A module with specific functionality (blog, shop, accounts, etc.).

```bash
python manage.py startapp myapp
# or
django-admin startapp myapp

```

### 4. Configure

```python
# Add app to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other apps
    'myapp',
]

# Configure templates directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "Templates"],
        # ... rest of config
    },
]

# Set custom user model (IMPORTANT: Do this before first migration)
AUTH_USER_MODEL = "myapp.CustomUser"

# Set login URL for @login_required decorator
LOGIN_URL = 'loginurl'

```

---

## Custom User Model

### Why Use Custom User?

- Add extra fields (age, profile_picture, phone_number, etc.)
- Change login field (use email instead of username)
- Customize authentication behavior

### 

```python
**from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        null=True,
        blank=True
    )
**
    # Add other custom fields here

```

**AbstractUser** includes standard fields:

- username
- email
- password
- first_name
- last_name
- is_staff
- is_active
- date_joined

---

## Database Setup

```bash
# Remove these before first migration (if starting fresh):
# - __pycache__ folders
# - db.sqlite3
# - migration files (except __init__.py)

# Create migration files
python manage.py makemigrations myapp

# Apply migrations
python manage.py migrate myapp
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

```

---

## Admin Panel Configuration

### 

```python
from django.contrib import admin
from myapp.models import CustomUser

# Register models for admin interface
admin.site.register([CustomUser])

```

This creates a control panel where you can add, edit, and delete data without writing extra code.

---

## Creating Views

### Signup View ()

```python
from django.shortcuts import render, redirect
from myapp.models import CustomUser
from django.contrib.auth import login, logout, authenticate

def signuppage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")

        # Validate username doesn't exist
        if CustomUser.objects.filter(username=username).exists():
            print("Username already exists.")
            return redirect("signupurl")

        # Validate passwords match
        if password == confirm_password:
            CustomUser.objects.create_user(
                username=username,
                password=password,
            )
            return redirect("loginurl")
        else:
            print("Passwords do not match")

    return render(req, "signup.html")

```

### Login View ()

```python
def loginpage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")

        # Authenticate user
        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)  # Create session
            return redirect("homeurl")

    return render(req, "login.html")

```

### Logout View ()

```python
def logoutpage(req):
    logout(req)  # End session
    return redirect("loginurl")

```

### Protected View with @login_required

```python
from django.contrib.auth.decorators import login_required

@login_required
def departmentpage(req):
    dept_data = Departmentmodel.objects.all()

    if req.method == "POST":
        name = req.POST.get("name")
        description = req.POST.get("description")
        Departmentmodel.objects.create(
            name=name,
            description=description,
        )

    context = {'dept_data': dept_data}
    return render(req, "department.html", context)

```

---

## Templates

### Signup Template (signup.html)

```html
<form action="" method="POST">
  {% csrf_token %}

  <label for="username">Username</label>
  <input type="text" name="username" placeholder="Your username.." required>

  <label for="password">Password</label>
  <input type="password" name="password" placeholder="Your password.." required>

  <label for="confirm_password">Confirm Password</label>
  <input type="password" name="confirm_password" placeholder="Confirm password.." required>

  <input type="submit" value="Sign Up">
  <a href="{% url 'loginurl' %}">Already have an account?</a>
</form>

```

### Login Template (login.html)

```html
<form action="" method="POST">
  {% csrf_token %}

  <label for="username">Username</label>
  <input type="text" name="username" placeholder="Your username.." required>

  <label for="password">Password</label>
  <input type="password" name="password" placeholder="Your password.." required>

  <input type="submit" value="Login">
</form>

```

### Navigation Template

```html
<div class="topnav">
  <a href="{% url 'homeurl' %}">Home</a>
  <a href="{% url 'signupurl' %}">Signup</a>
  <a href="{% url 'loginurl' %}">Login</a>
  <a href="{% url 'logouturl' %}">Logout</a>
</div>

```

---

## URL Configuration ()

```python
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signuppage, name="signupurl"),
    path('login/', loginpage, name="loginurl"),
    path('logout/', logoutpage, name="logouturl"),
    path('', homepage, name="homeurl"),
]

```

---

## Advanced Validation Example

```python
def sign_up_page(req):
    if req.method == "POST":
        full_name = req.POST.get('full_name')
        username = req.POST.get('username')
        phone_number = req.POST.get('phone_number')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        email = req.POST.get('email')

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            print("Username already exists.")
            return redirect("signupurl")

        # Validate password match
        if password == confirm_password:
            CustomUser.objects.create_user(
                username=username,
                full_name=full_name,
                phone_number=phone_number,
                email=email,
                password=password
            )
            return redirect("loginurl")
        else:
            print("Passwords do not match")

    return render(req, 'sign_up.html')

```

---

## Key Security Points

✅ **Always use `{% csrf_token %}`** in POST forms to prevent CSRF attacks

✅ **Use `method="POST"`** for sensitive data

✅ **Use `create_user()`** instead of `create()` - it automatically hashes passwords

✅ **Validate user input** before saving to database

✅ **Check username/email uniqueness** before creating accounts

✅ **Set `AUTH_USER_MODEL`** before first migration

---

## Common Django Auth Functions

| Function | Purpose |
| --- | --- |
| `authenticate()` | Verifies username/password |
| `login()` | Creates user session |
| `logout()` | Ends user session |
| `@login_required` | Restricts view to logged-in users |
| `create_user()` | Creates user with hashed password |
| `.exists()` | Checks if query returns any results |

---

This guide provides a complete foundation for implementing Django authentication in your projects! 🚀
