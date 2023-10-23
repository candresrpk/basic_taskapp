from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from applications.taski.forms import TaskForm
from applications.taski.models import Task
from django.utils import timezone


@login_required
def tasksView(request):
    tasks = Task.objects.filter(
        owner = request.user,
        datecompleted__isnull=True 
    )

    context = {
        'tasks':tasks,
        'title': 'pendientes'
    }
    return render(request, './taski/tasks.html', context)


@login_required
def completedTasksView(request):
    tasks = Task.objects.filter(
        owner = request.user,
        datecompleted__isnull=False 
    ).order_by('-datecompleted')

    context = {
        'tasks':tasks,
        'title': 'completadas'
    }
    return render(request, './taski/tasks.html', context)


@login_required
def createTasksView(request):
    context = {
        'form': TaskForm
    }

    if request.method == 'GET':
        return render(request, './taski/createTask.html', context)
    elif request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()

            return redirect('taskapp:tasks')
        
        except Exception as e:
            context['error'] = 'We got an error, please tray again later'
            return render(request, './taski/createTask.html', context)
    else:
        context['error'] = 'Sorry what was that?'
        return render(request, './taski/createTask.html', context)


@login_required
def detailTaskView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(instance=task)
    context = {
        'form':form,
        'task':task,
    }

    if request.method == 'GET':
        return render(request, 'taski/taskDetail.html', context)
    
    elif request.method == 'POST':
        try:
            new_task = TaskForm(request.POST, instance=task)
            new_task.save()
            return redirect('taskapp:tasks')
        except Exception as e:
            context['error'] = 'Sorry we got an error traying to update your task :c'
            return render(request, 'taski/taskDetail.html', context)
    else:
        context['error'] = 'Sorry what was that?'
        return render(request, 'taski/taskDetail.html', context)
    

@login_required
def completeTaskView(request, task_id):
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
    context = {
        'task':task,
    }

    if request.method == 'POST':
        try:
            task.datecompleted = timezone.now()
            task.save()
            return redirect('taskapp:tasks')
        except Exception as e:
            context['error'] = 'Sorry we got an error traying to update your task :c'
            return render(request, 'taski/taskDetail.html', context)
            
    else:
        context['error'] = 'Sorry what was that?'
        return render(request, 'taski/taskDetail.html', context)


@login_required
def deleteTaskView(request, task_id):
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
    context = {
        'task':task,
    }

    if request.method == 'POST':
        try:
            task.delete()
            return redirect('taskapp:tasks')
        except Exception as e:
            context['error'] = 'Sorry we got an error traying to update your task :c'
            return render(request, 'taski/taskDetail.html', context)
            
    else:
        context['error'] = 'Sorry what was that?'
        return render(request, 'taski/taskDetail.html', context)
