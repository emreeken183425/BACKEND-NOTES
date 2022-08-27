from django.shortcuts import render,redirect
from .models import Student_table
from .forms import Student_form
# Create your views here.
def home(request):
    return render(request,"student/index.html")

#----------------CRUD-----------------#

#read(GET)

def student_list(request):
    student=Student_table.objects.all() 
    context={
        'student':student
    }
    return render(request,"student/student_list.html",context)
    
#----------------CRUD-----------------#

#read(CREATE)

def student_add(request):
    # form=Student_form()
    # if request.method=="POST":
    #      print(request.POST)

    form=Student_form(request.POST or None ) 
    if form.is_valid():
        form.save()
        return redirect("list")
   

    context={
        'form':form
    }

    return render(request,"student/student_add.html",context)

#----------------CRUD-----------------#

#read(UPDATE)    

def student_update(request,id):
    student=Student_table.objects.get(id=id)
    form=Student_form(instance=student)
    
    if request.method=="POST":
        form=Student_form(request.POST,instance=student) 
        if form.is_valid():
           form.save()
        return redirect("list")

    context={
        'form':form
    }    

    return render(request,"student/student_update.html",context)

#----------------CRUD-----------------#

#read(UPDATE)  

def student_delete(request,id):
    student=Student_table.objects.get(id=id)
    
    if request.method=="POST":
        student.delete()
        return redirect("list")

    context={
        'student':student
    }    

       
    return render(request,"student/student_delete.html",context)   


    

