

from django.urls import path
# http://127.0.0.1:8000/  => anasayfa
# http://127.0.0.1:8000/home =>anasayfa

from .import views


urlpatterns = [
  
    path('list',views.kurslar),
    path('<kurs_adi>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategoryname,name='courses_by_category'),
    





    


   
]
