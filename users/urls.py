from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #start URL authorization as default
    path('', include('django.contrib.auth.urls')),
    #register page
    path('register/', views.register, name='register'),
]