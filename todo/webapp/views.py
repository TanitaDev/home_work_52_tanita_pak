from django.shortcuts import render

from webapp.models import Todo


def index_view(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)
