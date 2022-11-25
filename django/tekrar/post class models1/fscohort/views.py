from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    print(request)
    print(request.method)
    print(request.COOKİES)
    print(request.path)
    print(request.user)
    print(request.META)
    
    html="<html><body>helo fs </body> </html>"
    return HttpResponse(html)

  