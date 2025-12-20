from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal, Curso, Matricula, Alumno 
from .forms import SucursalForm, CursoForm, MatriculaForm, AlumnoForm
# Create your views here.

#Crud Sucursal

def sucursal_listar(request):
    sucursales = Sucursal.objects.all()
    return render(request, "sucursal/lista.html", {"sucursales": sucursales})


def sucursal_crear(request):
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sucursal_listar")
    else:
        form = SucursalForm()
    return render(request, "sucursal/form.html", {"form": form})


def sucursal_editar(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == "POST":
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect("sucursal_listar")
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, "sucursal/form.html", {"form": form})


def sucursal_eliminar(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == "POST":
        sucursal.delete()
        return redirect("sucursal_listar")
    return render(request, "sucursal/confirmar_eliminar.html", {"sucursal": sucursal})


#Crud Curso

def curso_listar(request):
    cursos = Curso.objects.all()
    return render(request, "curso/lista.html", {"cursos": cursos})


def curso_crear(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_listar")
    else:
        form = CursoForm()
    return render(request, "curso/form.html", {"form": form})


def curso_editar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("curso_listar")
    else:
        form = CursoForm(instance=curso)
    return render(request, "curso/form.html", {"form": form})


def curso_eliminar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        curso.delete()
        return redirect("curso_listar")
    return render(request, "curso/confirmar_eliminar.html", {"curso": curso})


#Crud Alumno

def alumno_listar(request):
    alumnos = Alumno.objects.all()
    return render(request, "alumno/lista.html", {"alumnos": alumnos})


def alumno_crear(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumno_listar")
    else:
        form = AlumnoForm()
    return render(request, "alumno/form.html", {"form": form})


def alumno_editar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("alumno_listar")
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, "alumno/form.html", {"form": form})


def alumno_eliminar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        alumno.delete()
        return redirect("alumno_listar")
    return render(request, "alumno/confirmar_eliminar.html", {"alumno": alumno})

#Crud Matricula

def matricula_listar(request):
    matriculas = Matricula.objects.select_related("alumno", "curso")
    return render(request, "matricula/lista.html", {"matriculas": matriculas})


def matricula_crear(request):
    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("matricula_listar")
    else:
        form = MatriculaForm()
    return render(request, "matricula/form.html", {"form": form})


def matricula_eliminar(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)
    if request.method == "POST":
        matricula.delete()
        return redirect("matricula_listar")
    return render(request, "matricula/confirmar_eliminar.html", {"matricula": matricula})

def matricula_editar(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)

    if request.method == "POST":
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect("matricula_listar")
    else:
        form = MatriculaForm(instance=matricula)

    return render(request, "matricula/form.html", {
        "form": form
    })

#-----------------------------------#
def alumnos_por_curso(request, curso_id):
    curso = get_object_or_404(Curso, codigo=curso_id)
    matriculas = Matricula.objects.filter(curso=curso).select_related('alumno')

    return render(request, 'curso/alumnos_curso.html', {
        'curso': curso,
        'matriculas': matriculas
    })
    
def matriculas_por_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, codigo=sucursal_id)
    
    matriculas = Matricula.objects.filter(
        sucursal=sucursal
    ).select_related('alumno', 'curso')

    return render(request, 'sucursal/matriculas_por_sucursal.html', {
        'sucursal': sucursal,
        'matriculas': matriculas
    })

def home(request):
    return render(request, "home.html")