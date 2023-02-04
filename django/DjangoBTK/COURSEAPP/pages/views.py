from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Create your views here.
def home(req):
    return HttpResponse('anasayfa')
def iletisim(req):
    return HttpResponse('iletişim listesi')

def hakkimizda(req):
    return HttpResponse('hakkımızda listesi')    