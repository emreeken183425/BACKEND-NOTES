from django.shortcuts import render,redirect
from .models import Member, Student
from .forms import StudentForm
from .forms import MemberForm
def index(request):
    return render(request, 'tekrar/index.html')

def student_list(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'tekrar/student_list.html',context) 

def Student__add(request):
    form=StudentForm()
    if request.method=="POST":
        print(request.POST)
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
        'form':form 
    }
    return render(request,'tekrar/student_add.html',context)

def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'tekrar/student_update.html', context)
        
def student_delete(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        student.delete()
        return redirect('list')
    return render(request,'tekrar/student_delete.html')        
        
def member_list(request):
    members=Member.objects.all()
    context={
        'members':members
    }        
    return render(request,'tekrar/member_list.html',context)




