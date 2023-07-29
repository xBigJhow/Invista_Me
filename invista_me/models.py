from django.db import models
from datetime import datetime

# Create your models here.
class Investimento(models.Model): #Herda do Models.Model para conseguir utilizar o banco de dados
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

