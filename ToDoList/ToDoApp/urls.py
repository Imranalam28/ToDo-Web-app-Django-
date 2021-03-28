from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('',views.ToDo,name='ToDoApp')
]