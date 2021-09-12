from django.conf import settings
from django.db import models


class Flashcard(models.Model):
    disciplina = models.ForeignKey('Disciplinas.Disciplina', on_delete=models.CASCADE)
    termo = models.CharField(max_length=200)
    define  = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.termo
