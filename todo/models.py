from django.db import models

# Create your models here.
class ToDo(models.Model):
    Titulo = models.CharField(max_length=250, blank=False)
    Descricao = models.TextField(blank=True)
    Data = models.DateField(blank=False)
    Completado = models.BooleanField(default=False)

    def __str__(self):
        return self.Titulo
