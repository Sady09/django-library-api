import uuid
from django.db import models

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=200, unique=True)
    autor = models.CharField(max_length=100)
    ano_de_leitura = models.IntegerField()
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    comentario = models.TextField()

    def __str__(self):
        return self.titulo