from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Maps to the home page
    path('upload/', views.upload, name='upload'),  # Maps to the upload documents page
    path('map/', views.map, name='map'),  # Maps to the map view page
    path('services/', views.services, name='services'),  # Maps to find surveyors page
    path('contact/', views.contact, name='contact'),  # Maps to the contact page
    path('login/', views.login, name='login'),  # Maps to login page
    path('signup/', views.signup, name='signup'),  # Maps to the register page
]
