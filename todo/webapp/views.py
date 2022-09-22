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


def update_todo_view(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update_todo.html', context)


def delete_todo_view(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'index.html', context)
