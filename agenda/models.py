from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    celular = models.CharField(max_length=9, verbose_name="Celular")
    telefone = models.CharField(max_length=9, verbose_name="Tel.Fixo")
    SEXO = (
        ('HOMEM', 'Homem'),
        ('MULHER', 'Mulher'),
    )
    sexo = models.CharField(max_length=6, choices=SEXO)

    def __str__(self):
        return self.nome
