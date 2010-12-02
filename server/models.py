from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()
    estoque = models.IntegerField()
