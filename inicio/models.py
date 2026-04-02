from django.db import models

# Create your models here.
class DepartamentosMedicos(models.Model):
    nombre = models.CharField(max_length=50)
    nro_departamento = models.IntegerField(unique=True)
    nro_medicos = models.IntegerField(null=True)
    fecha = models.DateField(auto_now_add=True)
    email_departemento = models.EmailField()
    
    def __str__(self):
        return f"Departamento: {self.nombre} - Nro: {self.nro_departamento}"


