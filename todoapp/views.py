from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Todo

# Create your views here.

def home(request):
    todos = Todo.objects
    return render(request, 'home.html',{'todos':todos})

def detail(request):
    todo_detail = get_object_or_404(Todo, pk = todo_id)
    return render(request,'detail.html',{'todo': todo_detail})

def new (request):
    return render(request, 'new.html')

def create(request):
    todo = Todo()
    todo.title = request.GET['title']
    todo.deadline = request.GET['deadline']
    todo.save()
    return render(request, 'new.html')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk = todo_id)
    todo.delete()
    return redirect(home)


def edit(request, todo_id):
    if(request.method =='POST'):
        todo= get_object_or_404(Todo, pk = todo_id)
        return render(request, 'edit.html',{'todo':todo})
    
def update(request, todo_id):
    todo = get_object_or_404(Todo, pk = todo_id)
    if(request.method =='POST'):
        todo.title = request.POST['title']
        todo.deadline = request.POST['deadline']
        todo.save()
        return redirect(home)