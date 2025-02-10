from django.db import models

#Create your models here

class Produto(models.Model):
    nome= models.charField(max_length=100)
    preco= models.DecimalField(max_digits=10, decimal_places=2)