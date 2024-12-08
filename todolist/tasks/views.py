from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import TaskForm

def task_list(request):
    if request.method == 'POST':  # Handle task creation
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    if request.method == 'GET':
          # Handle task listing
        form = TaskForm()
        tasks = Task.objects.all()
        context = {'tasks': tasks, 'form': form}
        return render(request, 'tasks/task_list.html', context)


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':  # Update the task
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:  # Display the current task for editing
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'tasks/task_form.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':  # Confirm and delete the task
        task.delete()
        return redirect('task_list')
    
    context = {'task': task}
    return render(request, 'tasks/task_confirm_delete.html', context)
