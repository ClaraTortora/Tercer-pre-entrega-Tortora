from django.shortcuts import render, redirect
from . import forms 


# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')


def crear_profesor(request):
    if request.method == 'POST':
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:index')
    else:
        form = forms.ProfesorForm()
        context = {'form': form}
    return render(request, 'inicio/crear_profesor.html', context)


def crear_alumno(request):
    if request.method == 'POST':
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:index')
    else:
        form = forms.AlumnoForm()
        context = {'form': form}
    return render(request, 'inicio/crear_alumno.html', context)


def crear_materias(request):
    if request.method == 'POST':
        form = forms.MateriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:index')
    else:
        form = forms.MateriasForm()
        context = {'form': form}
    return render(request, 'inicio/crear_materias.html', context)


