from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = TaskForm()   

    ctx = {'tasks': tasks, 'form': form}
    return render(request, "tasks/index.html", ctx)

def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("index")

    form = TaskForm(instance=task)

    ctx = {"form": form}
    return render(request, "tasks/update_task.html", ctx)


def delete(request, pk):
    item = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("index")

    ctx = {"item": item}

    return render(request, "tasks/delete.html", ctx)