from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Apelido/Usuário', max_length=30, unique=True, help_text='Username')
    name = models.CharField('Nome', max_length=100)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plurral = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self) 

    def get_short_name(self):
        return str(self).split(" ")[0]           
