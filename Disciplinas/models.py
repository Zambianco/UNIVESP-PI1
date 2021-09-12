from django.conf import settings
from django.db import models


class Disciplina(models.Model):
    codigo = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.codigo
