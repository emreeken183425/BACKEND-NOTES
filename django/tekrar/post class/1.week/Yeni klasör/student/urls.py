from django.urls import path
from .views import home, about

urlpatterns = [
    
    path("fs/", home, name="home" ),
    path("be/", about, name="about" ),
]