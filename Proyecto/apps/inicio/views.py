from django.shortcuts import render, redirect
from .import forms

# Create your views here.
def index(request):
    return redirect('inicio:index')

def crear_profesor(request):
    if request.method == 'POST':
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio/index.html')
    else:
        form = forms.ProfesorForm()
        context = {'form': form}
    return render (request, 'inicio/crear_profesor.html', context)