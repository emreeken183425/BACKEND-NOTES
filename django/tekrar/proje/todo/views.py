from django.shortcuts import render
from .models import Category, Todo
from .serializers import TodoSerializers, CategorySerializers
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView



# crud islemlerinin hepsine izin veriyor. ViewsSet kullandık
class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers




# concrete Views (mixin ile genericview birleşimi) get ve post islemi sagliyor
class CategoryListCreate(ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializers


# concrete Views update ve delete islemi sagliyor
class CategoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset =Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = "id"





