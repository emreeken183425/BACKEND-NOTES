from django import forms 
from .models import Student,Member

class StudentForm(forms.ModelForm):
    
    class Meta:
        model=Student
        fields='__all__'
        labels={
            "first_name":"adınız",
            "last_name":"soyadınız",
            "number":"numaranız"
        }

class MemberForm(forms.ModelForm):
    
    class Meta:
        model:Member
        fields='__all__'
        labels={
            "number":"numara",
            "title":"başlık",
            "topic":"konu",
            "comment":"yorum"
            
        }

