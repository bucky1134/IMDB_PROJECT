#Building function based view only for register api .. as currently there is no login/logout facility is to be added

from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from user import views

# created two urls for login and register 
urlpatterns=[    
    path('register/',views.UserRegister,name="UserRegister"), 
    path('login/',obtain_auth_token,name="login")
]