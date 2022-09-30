from random import choices
from django.shortcuts import render

from list_app.models import Task, Choices


def index_view(request):
    tasks = Task.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks,
        'choices': Choices.choices
    }
    return render (request, 'index.html', context=context)
      