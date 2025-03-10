from django.db import models
from django.db.models import Model


# Create your models here.

class Curso(models.Model):
    id = models.CharField(max_length=4, blank=False, primary_key=True)
    nome = models.CharField(max_length=30, blank=False)
    carga_horaria = models.DecimalField(max_digits=4, decimal_places=2)
    preco = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'id:${self.id} - Nome do curso: ${self.nome} - carga horaria : {self.carga_horaria} - preço : ${self.preco} '

