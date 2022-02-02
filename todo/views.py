from multiprocessing import context
from django.shortcuts import redirect, render, redirect
from .models import tarea
from .forms import TareaForm
# Create your views here.

def home(request):
    tareas = tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'todo/home.html',context)

def agregar(request):
    if request.method == 'POST':
        form =TareaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context={'form':form}
    return render(request,'todo/agregar.html',context)

def eliminar(request, tarea_id):
    Tarea = tarea.objects.get(id=tarea_id)
    Tarea.delete()
    return redirect('home')

def editar(request, tarea_id):
    Tarea = tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST,instance=Tarea)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=Tarea)
        pass
    context={'form':form}
    return render(request,'todo/editar.html',context)