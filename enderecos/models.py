from django.db import models
#nem sempre um ponto turistico vai ter uma rua ou bairro entao dessa forma
#atende melhor a principio
class Endereco(models.Model):
    linha1 = models.CharField(max_length=150)#rua
    linha2 = models.CharField(max_length=150,null=True, blank=True)#bairro
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
