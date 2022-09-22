from django.shortcuts import render, redirect

from webapp.models import Todo
from .forms import *


def index_view(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)

