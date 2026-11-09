from django.shortcuts import render, redirect
from .models import *

def home_page(request):
    return render(request, 'home.html')


def get_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'gettask.html', {'task': tasks})



def add_task(request):
    if request.method == "POST":
        Task.objects.create(
            title=request.POST["title"],
            caption=request.POST["caption"],
            due_date=request.POST["due_date"])
        return redirect('show_task')
    return render(request, 'add_task.html')


def get_task_id(request, id):
    tasks = Task.objects.get(pk=id)
    return render(request, 'showtask_id.html', {'tasks': tasks})



def update_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        task.title = request.POST["title"]
        task.caption = request.POST["caption"]
        task.due_date = request.POST["due_date"]
        task.save()
        return redirect('show_task')
    return render(request, 'update_task.html',{'task': task})


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')