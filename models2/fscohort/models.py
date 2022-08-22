from django.db import models

class Student(models.Model):
    first_name = models.CharField('Adı',max_length=50)
    last_name = models.CharField( 'Soyadı',max_length=50)
    number=models.IntegerField('Numara')
