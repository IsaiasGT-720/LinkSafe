from django.db import models
from django.contrib.auth.models import User

## EN DJANGO NO SE CREAN USUARIOS, EL POR DEFECTO TRAE UN SISTEMA PARA MANEJAR USUARIOS.
## ESTE ARCHIVO LO CORREGISTE TÚ, PERO NO SÉ SI SERÁ SUFICIENTE.

class Link(models.Model):
    title = models.CharField(max_length=300)
    URL = models.URLField(null=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='links',
        null=True
    )

    def __str__(self):
        return self.title


