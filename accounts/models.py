from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template import Template
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class UserU(AbstractBaseUser, PermissionsMixin):

    name = models.CharField('name', max_length=100, blank=True,null=True)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=100, blank=True,null=True)
    username = models.CharField('name de Usuário', unique=True, max_length=100)
    birth_data = models.CharField('Data de Nascimento', max_length=100,blank=True)
    sex = models.CharField('Sexo',max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino')), default='Masculino')
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name']

    def __str__(self):
        return self.username

    def __unicode__(self):
        return u"username: %s " % (self.username or u'')

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Doctor(UserU):

    crm = models.CharField('CRM', max_length=100, unique=True)

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Allergy(models.Model):

    allergy_name = models.CharField('Nome da Alergia', max_length=100, blank=True,null=True)

    def __str__(self):
        return self.allergy_name

    def get_short_name(self):
        return self.allergy_name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Alergia'
        verbose_name_plural = 'Alergias'

class Patient(UserU):

    blood_type = models.CharField('Tipo Sanguíneo', max_length=100, blank=True,null=True)
    clinical_condition = models.CharField('Condições Clínicas', max_length=100, blank=True,null=True)
    medicine = models.ForeignKey("register.Medicine", verbose_name='Medicamentos',related_name='medicine_Patient', null=True, blank=True)
    allergy = models.ForeignKey(Allergy, verbose_name='Alergias',related_name='allergy_Patient', blank=True,null=True)
    comment = models.TextField('Observações', blank = True)
    weight = models.CharField('Peso', max_length=100, blank=True,null=True)
    height = models.CharField('Altura', max_length=100, blank=True,null=True)
    address = models.CharField('Endereço', max_length=300, blank=True,null=True)

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'



