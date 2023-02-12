from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from  django.urls import reverse
# Create your views here.

data={
    "programlama":"programlama kategorisine ait kurslar",
    "web-geliştime":"web-geliştime kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar"

    

}

def kurslar(req):
    list_items=""
    category_list=list(data.keys())

    for category in category_list:
        redirect_url=reverse('courses_by_category',args=[category])
        list_items +=f"<li><a href='{redirect_url }'>{category}</a></li> "
    html=f" <h1>kurslar listesi </h1> <br><ul>{list_items}</ul> "


    return HttpResponse(html)

def details(req,kurs_adi):
    return HttpResponse(f'{kurs_adi} details sayfası')

def getCoursesByCategoryname(req,category_name):
    try:
        category_text=data[category_name]   
    except:
        return HttpResponseNotFound("yanış kategori")    


  
    return  HttpResponse(category_text)
      

def getCoursesByCategoryId(req,category_id):
    category_list=list(data.keys())

    if(category_id>len(category_list)):

        return HttpResponseNotFound("yanlış kategori")

    category_name=category_list[category_id - 1]

    redirect_url=reverse('courses_by_category',args=[category_name])
    return redirect(redirect_url) 