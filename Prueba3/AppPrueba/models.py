from django.db import models

# Create your models here.
class Sucursal(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    
    def __str__(self):    
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    rut = models.CharField(max_length=10, primary_key=True)
    fono = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    codigo = models.AutoField(primary_key=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        db_column='curso_codigo'
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        db_column='alumno_rut'
    )
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        db_column='sucursal_codigo'
    )
    fecha = models.DateField()

    def __str__(self):
        return f"Matricula {self.codigo}"
