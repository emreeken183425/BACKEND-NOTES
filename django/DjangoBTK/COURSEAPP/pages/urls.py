

from django.urls import path
# http://127.0.0.1:8000/  => anasayfa
# http://127.0.0.1:8000/home =>anasayfa

from .import views


urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
   
    path('hakkimizda',views.hakkimizda),
    path('iletisim',views.iletisim),


   
]
