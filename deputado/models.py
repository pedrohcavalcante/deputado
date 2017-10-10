from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    nome_deputado = models.CharField(max_length=50)
    sigla_partido = models.CharField(max_length=5)
    nome_partido = models.CharField(max_length=50)
    Status = models.CharField(max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_deputado

class Link(models.Model):
    link_1 = models.CharField(max_length=50)
    destino = models.CharField(max_length=50, default='#')
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.link_1