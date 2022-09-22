from django.shortcuts import render

from webapp.models import Todo
from .forms import *


def index_view(request):
    todos = Todo.objects.all()

    form = TodoForm()
    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)
