from django.db import models

# Create your models here.
#CATEGORY TO DO

class Category(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Todo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,related_name="categorys")
    task=models.CharField(max_length=50)
    description=models.TextField()
    
    TITLE=[
        ("H","High"),
        ("M","Medium"),
        ("L","Low"),
           
           ]
    priority=models.CharField(max_length=18,choices=TITLE,default="L" )    
    is_done=models.BooleanField()
    createDate=models.DateTimeField(auto_now_add=True)
    updateDate=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.task} "