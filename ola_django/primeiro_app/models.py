from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome=models.CharField(max_length=45)
    idade=models.IntegerField()
    email=models.CharField(max_length=60)
    tipo_pessoa=models.ForeignKey('TipoPessoa', on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.nome

class TipoPessoa(models.Model):
    nome=models.CharField(max_length=45)
    descricao=models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.nome

class InteracoesPessoa(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora=models.DateTimeField(auto_now_add=True)
    mensagem=models.TextField()