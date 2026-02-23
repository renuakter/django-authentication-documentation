from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
def basepage(req):
    return render(req,"master/base.html")
def signinpage(req):
    if req.method == "POST":
        fullname = req.POST.get("fullname")
        email = req.POST.get("email")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")
        username = req.POST.get("username")

        # Username exists check
        if customuser.objects.filter(username=username).exists():
            messages.warning(req, "User already exists")
            return redirect("signinpage")

        # Password match check
        if password == confirm_password:
            customuser.objects.create_user(
                username=username,
                fullname=fullname,
                email=email,
                password=password,
            )
            messages.success(req, "User created successfully")
            return redirect("loginpage")

        else:
            messages.error(req, "Passwords do not match")
            return redirect("signinpage")

    # 🔥 IMPORTANT — GET request এর জন্য return
    return render(req, "auth/signin.html")

def loginpage(req):
     if req.method=="POST":
    
      
        password=req.POST.get("password")
        username=req.POST.get("username")
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            messages.success(req, "Login successful")
            return redirect("masterbase.html")
        messages.error(req, "Invalid username or password")
        return redirect("basepage")
     return render(req,"auth/login.html")
