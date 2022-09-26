from .serializers import TodoSerializers,CategorySerializers
from .models import Todo,Category
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

#! ModelViewSet --TO DO 
#? crud işlemlerinin hepsine izin veren yöntem 
class TodoModelViewSet(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers

# concrate apıview category
#! get ve post için 
class CategoryListCreate(ListCreateAPIView ):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
# update ve delete için 
class CategoryConcrateURD(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=RetrieveUpdateDestroyAPIView
    lookup_field="pk"

