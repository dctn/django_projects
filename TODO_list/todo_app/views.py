from django.shortcuts import render,HttpResponse
from .models import Todo_model
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
# Create your views here.
def index(request):
    data = Todo_model.objects.all()
    context = {
        "data":data
    }
    return render(request,"index.html",context)

def add_task(request):
    if request.method == "POST":
        todo = request.POST.get("task")

        data = Todo_model.objects.create(name=todo)
        data.save()
    data = Todo_model.objects.all()
    context = {
        "data":data
    }

    return render(request,'index.html',context)

@csrf_exempt
def edit_task(request,id):
    task_data = Todo_model.objects.get(pk=id)
    task_name = task_data.name

    return HttpResponse(request,f"<div><input type='text' id='task_input' value='{task_name}' autocomplete='off' name='task' placeholder='New task' required></div>")

@csrf_exempt
def delete_task(request,id):
    task = Todo_model.objects.get(pk=id)
    task.delete()
    data = Todo_model.objects.all()
    context = {
        "data":data
    }
    return render(request,'index.html',context)

@csrf_exempt
def checkbox(request,id):
    task = Todo_model.objects.get(pk=id)

    if task.checkbox == True:
        task.checkbox = False

    elif task.checkbox == False:
        task.checkbox = True

    task.save()

    data = Todo_model.objects.all()
    context = {
        "data":data
    }
    return render(request,'index.html',context)