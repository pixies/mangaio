from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	apelido = models.OneToOneField(User)
	nome = models.CharField('Primeiro nome', max_length=200)
	snome = models.CharField('Sobrenome', max_length=200)
	email = models.EmailField('Email', max_length=200)
	
	def __str__(self):
		return self.nome

class Endereco(models.Model):
	logradouro = models.CharField('Logradouro', max_length=200)
	bairro = models.CharField('Bairro', max_length=200)
	cidade = models.CharField('Cidade', max_length=200)
	numero = models.CharField('Numero', max_length=7)
	complemento = models.CharField('Complemento', max_length=200)
	cep = models.CharField('CEP', max_length=9)

	def __str__(self):
		return self.cidade

class RedeSocial(models.Model):
	nome_rede = models.CharField('Nome da rede', max_length=200)

	def __str__(self):
		return self.nome_rede

class UserProfile(models.Model):
	usuario = models.ForeignKey(Usuario)

	escolhasexo = (
		('M', 'Masculino'),
		('F', 'Feminino'),
		('O', 'Outros'),
		('---', 'Escolha a opção')
		)
	sexo = models.CharField(
		'Sexo',
		max_length=3,
		choices=escolhasexo,
		default='---',
		)
	endereco = models.ForeignKey(Endereco)

	phone = models.CharField('Telefone', max_length=15)

	genero_favorito = models.CharField('Gênero favorito', max_length=200)

	redes_sociais = models.ManyToManyField(RedeSocial)

	bio = models.TextField('Fale sobre você')

	def __str__(self):
		return self.usuario.nome