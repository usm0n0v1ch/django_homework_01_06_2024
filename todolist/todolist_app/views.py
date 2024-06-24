from django.shortcuts import render, redirect, get_object_or_404

from todolist_app.forms import TaskForm
from todolist_app.models import Task


# Create your views here.

def task_list(request):
    tasks = Task.objects.exclude(completed=True).values('id', 'title', 'description')
    for task in tasks:
        print(f'Task ID: {task["id"]}, Task Title: {task["title"]}')
    ctx = {
        'tasks': tasks
    }
    return render(request, 'todolist_app/task_list.html', context=ctx)

# def task_list(request):
#    #Выбераем только часть колонок из таблицы
#     tasks = Task.objects.all().values('title', 'completed')
#     ctx = {
#         'tasks': tasks
#     }
#     return render(request, 'todolist_app/task_list.html', context=ctx)
# def task_list(request):
#     # Исключаем завершенные задачи из списка
#     tasks = Task.objects.exclude(completed=True).values('title', 'description')
#     ctx = {
#         'tasks': tasks
#     }
#     return render(request, 'todolist_app/task_list.html', context=ctx)
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    ctx = {
        'form': form
    }
    return render(request, 'todolist_app/task_form.html', context=ctx)

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    ctx = {
        'form': form
    }
    return render(request, 'todolist_app/task_form.html', context=ctx)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    ctx = {
        'task': task
    }
    return render(request, 'todolist_app/task_delete.html', context=ctx)