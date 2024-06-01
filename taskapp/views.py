from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'taskapp/index.html', context)


def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')