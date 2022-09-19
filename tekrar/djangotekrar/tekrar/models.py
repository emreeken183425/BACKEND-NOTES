from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    number=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Member(models.Model):
    title=models.CharField(max_length=50)
    topic=models.CharField(max_length=50)
    comment=models.CharField(max_length=200)
    number=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return f" {self.number} {self.title} {self.topic} {self.comment} "
        