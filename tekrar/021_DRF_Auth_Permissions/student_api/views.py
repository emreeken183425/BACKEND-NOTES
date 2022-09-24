from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

#! IsAuthenticated 👉 A user who is not logged in cannot make get and post requests.
#! IsAdminUser 👉 Only an admin user can make a get and post requests.
#! IsAuthenticatedOrReadOnly 👉 If the user is not logged in, he/she can only make a get request.
# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes=[IsAuthenticated]

       

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()