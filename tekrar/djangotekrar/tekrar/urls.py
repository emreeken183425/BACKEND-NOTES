from django.urls import path
from .views import index,student_list,Student__add,student_update,student_delete,member_list

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list,name='list' ),
    path('add/',Student__add,name='add'),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete,name="delete"),
    path('member/',member_list,name="member")
    ]