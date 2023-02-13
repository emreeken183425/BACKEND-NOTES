

from django.urls import path
# http://127.0.0.1:8000/  => anasayfa
# http://127.0.0.1:8000/home =>anasayfa

from .import views


urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('about',views.about),
    path('contact',views.contact),


   
]
