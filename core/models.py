from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario
from avaliacao.models import Avaliacao
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos',null=True,blank=True)
    def __str__(self):
        return self.nome
