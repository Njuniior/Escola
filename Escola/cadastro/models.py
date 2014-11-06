#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES


# Create your models here.


class Cadastro(models.Model):
	
	Nome = models.CharField('Nome',max_length=100,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Endereco = models.CharField('Endereço',max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=STATE_CHOICES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)	

 	def __unicode__(self):
		return self.Nome