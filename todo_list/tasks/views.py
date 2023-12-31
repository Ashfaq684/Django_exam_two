from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = TaskModel.objects.get(pk = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form' : form})

def complete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('show_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'tasks': tasks})