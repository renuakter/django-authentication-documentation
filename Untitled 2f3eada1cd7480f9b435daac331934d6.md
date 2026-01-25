# Untitled

**Django Authentication Setup**

**Introduction:** Authentication verifies a user's identity. In web applications, it ensures only authorized users can access certain pages or perform specific actions. It keeps your website secure and protects sensitive information.

Django's authentication framework lets developers easily:

- Create and manage user accounts
- Allow users to **log in, log out, and register** securely
- Restrict access to views using decorators like **@login_required**
- Manage **permissions** and **user roles** through the admin panel

## **Virtual Environment**

- A virtual environment is an isolated workspace for a Python project.
- It lets you install and manage project packages independently from other projects or the system Python installation.
- This keeps dependencies organized, secure, and separated, preventing conflicts between projects.

### **1. Create Virtual Environment**

***python -m venv myenv***

To activate the environment, use this command:

***.\myenv\Scripts\activate***

Deactivate when done:

***.\myenv\Scripts\deactivate***

### **2. Install Django**

Download and install Django into your Python environment:

***pip install django***

### **3. Create Project and App**

**Project:**

- A project is the overall website or application. It contains settings, URLs, and configuration for the whole site.

***django-admin startproject myproject***

**App:**

An app is a smaller module within the project. Each app has specific functionality like blog, shop, or accounts. You can create multiple apps in one project and reuse them in other projects.

***python manage.py startapp myapp*** or ***django-admin startapp myapp***

### **4. [settings.py](http://settings.py/)**

# Add 'myapp' to **INSTALLED_APPS**

*INSTALLED_APPS = [*

*'myapp',*

*]*

# Ensure **TEMPLATES DIRS** includes **BASE_DIR / 'Templates'**

*TEMPLATES = [*

*{*

*'BACKEND': 'django.template.backends.django.DjangoTemplates',*

*'DIRS': [BASE_DIR,"Templates"],*

## 

## **AbstractUser in Django**

- **AbstractUser** is a built-in base class for Django's User model.
- It includes standard fields: **username, email, password, first_name, last_name,** etc.
- You can extend it to add extra fields for your project.

**Custom User in Django:**

- A **custom user** is a user model you define yourself, usually by extending AbstractUser or AbstractBaseUser.
- Use a custom user when the default User model doesn't fit your needs—for example, if you want email as the login field instead of username, or need extra fields like age or profile_picture.
- To use a custom user, set it in [settings.py](http://settings.py)

### **5. Creating [models.py](http://models.py/)**

In [models.py](http://models.py/), first import **AbstractUser** from django.contrib.auth.models:

*from django.contrib.auth.models import AbstractUser*

*# Create your models here.*

*class CustomUser(AbstractUser):*

*User_Type=models.CharField(choices=USER,max_length=100,null=True)*

# Ensure [**settings.py**](http://settings.py/) includes **AUTH_USER_MODEL = "myapp.CustomUser"**

***AUTH_USER_MODEL="myapp.CustomUser"***

### **6. Makemigrations and Migrate in Django**

**makemigrations** → writes instructions for database changes

**migrate** → applies those instructions to the database

Before running makemigrations and migrate, remove **pycache**, db.sqlite3, and migration files:

- ***python manage.py makemigrations myapp***
- ***python manage.py migrate myapp***
- ***python manage.py migrate***

# **7. Create Superuser in Django**

This creates a user with full permissions (read, add, edit, delete) for all models in your project. The superuser can log into the Django Admin interface:

***python manage.py createsuperuser***

# **8. admin.py Working Process in Django**

**admin.py** is where you control your data from the Django admin interface.

- You can add, edit, and delete data without writing extra code.
- It's like a control panel for your app's database.

***from django.contrib import admin***

***from myapp.models import ****

***# Register your models here.***

***admin.site.register([CustomUser])***

### **9. Creating Templates**

### **How Templates Work**

1️⃣ Create a template file (.html) in the Templates/ folder.

2️⃣ In your view (Python code), tell Django which template to use.

3️⃣ Django fills the template with data and displays it on the website.

### **Signup**

Ensure **method="POST"** and **{% csrf_token %}** are included.

**method="POST"** → Sends data securely to the server.

**{% csrf_token %}** → Django requires this to protect against CSRF attacks.

### **Signup.html:**

***<form action="" method="POST" enctype="multipart/form-data">***

***{% csrf_token %}***

***<label for="lname"**>Username**</label>***

***<input type="text" id="lname" name="username" placeholder="Your username..">***

***<label for="lname">Password</label>***

***<input type="password" id="lname" name="password" placeholder="Your password..">***

***<label for="lname">Confirm Password</label>***

***<input type="password" id="lname" name="confirm_password" placeholder="Your confirm password..">***

***<input type="submit" value="Sign Up">***

***<a href="{% url 'loginurl' %}">Already have an account</a>***

***</form>***

### **views.py: Working Process**

[views.py](http://views.py) is the brain of your app. It decides what to show when someone visits a webpage.

**1️⃣ User sends a request**

- When someone opens a URL in the browser, Django sends the request to the view associated with that URL.

**2️⃣ View processes the request**

The function or class in [views.py](http://views.py) can:

- Get data from the database
- Process forms
- Apply logic like authentication
- Prepare information to display on a page

**3️⃣ View returns a response**

Usually, the view renders a template. (The **render** function combines a template with data and sends it to the user's browser.)

**views.py**

***from django.shortcuts import render,redirect***

***from myapp.models import ****

***from django.contrib.auth import login,logout,authenticate***

***from django.contrib.auth.decorators import login_required***

***# Create your views here.***

***def signuppage(req):***

***if req.method == 'POST':***

***username = req.POST.get("username")***

***password = req.POST.get("password")***

***confirm_password = req.POST.get("confirm_password")***

***if password == confirm_password:***

***CustomUser.objects.create_user(***

***username=username,***

***email=email,***

***password=password,***

***)***

***return redirect("loginurl")***

***else:***

***print("Passwords do not match")***

***return render(req, "signup.html")***

### [**urls.py**](http://urls.py/)

**urls.py** is like a map for your website. It tells Django which page (view) to show when someone visits a specific URL.

**Connect URL:**

**{% url 'url_name' %}**

### **How It Works**

1️⃣ Define URLs in **urls.py**

2️⃣ Each URL is connected to a view in **views.py**

3️⃣ When a user visits a URL, Django finds the view and displays the page

*from django.contrib import admin*

*from django.urls import path*

*from myapp.views import **

*urlpatterns = [*

*path('admin/', admin.site.urls),*

*path('',signuppage, name="signupurl"),*

*]*

### **Login**

[**settings.py**](http://settings.py/): Set the login URL

***LOGIN_URL='log_in'***

### **login.html**

***<form action="" method="POST">***

***{% csrf_token %}***

***<label for="lname">Username</label>***

***<input type="text" id="lname" name="username" placeholder="Your username..">***

***<label for="lname">Password</label>***

***<input type="password" id="lname" name="password" placeholder="Your password..">***

***<input type="submit" value="Sign Up">***

***</form>***

[**views.py**](http://views.py/):

**from django.contrib.auth import login,logout,authenticate**

***def loginpage(req):***

***if req.method =='POST':***

***password=req.POST.get("password")***

***username= req.POST.get("username")***

***user = authenticate(req,***

***username=username,***

***password=password,***

***)***

***if user:***

***login(req,user)***

***return redirect("homeurl")***

***return render(req,"login.html")***

[**urls.py**](http://urls.py/):

***path('login/',loginpage, name="loginurl"),***

### **Logout**

[**views.py**](http://views.py/):

***def logoutpage(req):***

***logout(req)***

***return redirect("loginurl")***

[**urls.py**](http://urls.py/):

***path("logout/",logoutpage,name="logouturl"),***

### **Login_required**

**@login_required** is a decorator that ensures a page is only visible to logged-in users.

First, import this function from Django:

**from django.contrib.auth.decorators import login_required**

*@login_required*

*def departmentpage(req):*

*dept_data=Departmentmodel.objects.all()*

*if req.method=="POST":*

*name=req.POST.get("name")*

*description=req.POST.get("description")*

*Departmentmodel.objects.create(*

*name=name,*

*description=description,*

*)*

*context={*

*'dept_data':dept_data,*

*}*

*return render(req,"department.html",context)*

### **Add Navigation**

Add links for Signup, Login, Logout, and Home in your base template or navbar HTML:

*<div class="topnav">*

*<a class="active" href="#home">home</a>*

*<a href="{% url 'signuppageurl' %}">signup</a>*

*<a href="{% url 'loginpageurl' %}">login</a>*

*<a href="{% url 'logoutpageurl' %}">logout</a>*

*</div>*

### **Validation**

Use conditions for validation.

If a user exists, first filter:

**username_exist = EventUserModel.objects.filter(username=username).exists()**

Then use this condition:

**if username_exists:**

**print("Username already exists.")**

**return redirect("signupurl")**

Save the field using create, then:

**else:**

**print("Passwords do not match")**

Full code:

**def sign_up_page(req):**

**if req.method == "POST":**