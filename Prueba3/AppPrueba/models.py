from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name="cursos"
    )

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name="matriculas"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="matriculas"
    )
    fecha_matricula = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("activa", "Activa"),
            ("cancelada", "Cancelada"),
        ],
        default="activa"
    )

    def __str__(self):
        return f"{self.alumno} - {self.curso}"
