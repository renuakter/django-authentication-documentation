
from django.urls import path,include
from myapp.views import *
urlpatterns = [
path('basepage/', basepage, name="basepage"),
path('signinpage/', signinpage, name="signinpage"),
path('loginpage/', loginpage, name='loginpage'),
]