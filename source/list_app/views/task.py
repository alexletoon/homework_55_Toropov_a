
from http.client import HTTPResponse
import re
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseNotFound
from list_app.models import Task

from datetime import datetime

from list_app.models import Choices



def add_task_view(request):
    if request.method =='GET':
        context = {'choices': Choices.choices}
        return render(request, 'new_task.html', context=context)
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline_date': request.POST.get('date'),
        'task': request.POST.get('task')
    }
    task = Task.objects.create(**task_data)
    return redirect(reverse('index_view'))


def display_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task": task,
        'choices': Choices.choices
    }
    return render(request, 'task.html', context=context)


def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk )
    if request.method == 'POST':
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline_date = request.POST.get('date')
        task.task = request.POST.get('task')
        task.save()
        return redirect ('task_view', pk=task.pk)
    return render(request, 'update_task.html', context={'task': task, 'choices': Choices.choices})
