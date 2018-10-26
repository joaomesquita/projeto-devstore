from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from localflavor.br.br_states import STATE_CHOICES
import re

# Create your views here.
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )
    username = models.CharField('Usuário', max_length=30, unique=True, validators=[
        validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Informe um nome de usuário válido. Este valor deve conter apenas letras, números e os caracteres: @/./+/-/_.', 'invalid')
    ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma')
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=14)
    gender = models.CharField('Sexo', max_length=1, choices=GENDER_CHOICES)
    telephone = models.CharField('Telefone', max_length=11, blank=True)
    birth = models.DateField('Data de Nascimento', blank=True, null=True)
    street = models.CharField('Rua', max_length=100)
    number = models.CharField('Número', max_length=5)
    complement = models.CharField('Complemento', max_length=50)
    district = models.CharField('Bairro', max_length=50)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField('CEP', max_length=9)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
