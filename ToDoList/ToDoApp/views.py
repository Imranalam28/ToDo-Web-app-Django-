from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item


def ToDo(request):
    all_item = Item.objects.all()

    return render(request,'todo.html',{'items':all_item})


def add(request):
    cn = request.POST['content']
    item = Item(text = cn)
    item.save()
    return HttpResponseRedirect('/ToDoApp/')

def delete_item(request,ID):
    del_item = Item.objects.get(id = ID)
    del_item.delete()
    return HttpResponseRedirect('/ToDoApp/')

