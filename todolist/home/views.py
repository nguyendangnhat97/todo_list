from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from home.models import Task

# Create your views here.

def home(request):
    context = {'success': False}
    if request.method == "POST":
        # Handle the form 
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}


    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all() #fetch all tasks in db
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

# @csrf_exempt
def delete_todo(request, todo_id):
    Task.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/tasks")