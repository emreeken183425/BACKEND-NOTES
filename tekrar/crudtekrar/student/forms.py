from django import forms
from .models import Student_table

class Student_form(forms.ModelForm):
    class Meta:
        model=Student_table
        fields="__all__"
# fields = ["first_name", "last_name"]
        # labels = {"last_name" : "Surname"} labels değiştirebiliyoruz