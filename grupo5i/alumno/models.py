from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_lenght=75, verbose_name="Nombre")
    apaterno = models.CharField(max_lenght=75, verbose_name="Apaterno")
    amaterno = models.CharField(max_lenght=75, verbose_name="Amaterno")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=False, blank=False)
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso", null=False, blank=False)
    
    class Meta: 
        db_table="Alumnos"
        verbose_name="Alumno"
        verbose_name="Alumnos"
        
        def __str__(self) -> str:
        return self.nombre
    
    class Frase(models.model):
        comentario=models.TextField(verbose_name="comentario")