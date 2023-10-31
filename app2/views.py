from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
import datetime

# Create your views here.

def task_form(request):
    return render(request, 'add_task.html')

def add_task(request):
    now = datetime.datetime.now()

    if request.method == 'POST':
        t = request.POST['task']
        c = request.POST['category']
        d = request.POST['duedate']
        n = request.POST['note']
        p = request.POST['progress']

        b1 = task.objects.create(task=t, category=c, duedate=d, note=n, progress=p, modified=now)
        b1.save()
        return redirect('/')
    else:
        return HttpResponse("get method")

def get_list(request):
    content = {}
    content['data'] = task.objects.all()
    return render(request, 'dashboard.html',content)


def delete(request,rid):
    x = task.objects.get(id=rid)
    x.delete()
    return redirect('/')

def edit(request,rid):
    now = datetime.datetime.now()

    if request.method == 'POST':
        t = request.POST['task']
        c = request.POST['category']
        d = request.POST['duedate']
        n = request.POST['note']
        p = request.POST['progress']
        #m = request.POST['modified']

        b = task.objects.filter(id=rid)
        b.update(task=t, category=c, duedate=d, note=n, progress=p, modified=now)
        return redirect('/')
    else:    
        content = {}
        content['data'] = task.objects.get(id=rid)
        return render(request, 'edit_task.html', content)
