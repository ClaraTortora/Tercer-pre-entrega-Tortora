from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_profesor/', views.crear_profesor, name='crear_profesor'),
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'), 
    path('crear_materias/', views.crear_materias, name='crear_materias'),
]