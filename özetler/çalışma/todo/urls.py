from django.urls import path,include
from rest_framework import routers
from .views import (
    TodoModelViewSet,
    CategoryListCreate,
    CategoryConcrateURD
)

#router = routers.SimpleRouter()
router=routers.DefaultRouter()
router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    
    #CBV Concrate view
    path('list/',CategoryListCreate.as_view()),
    path('list/<int:pk>',CategoryConcrateURD.as_view())
    
    
    ]
