from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/', include('student.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

