from django.db import models
from django.conf import settings
from django.db.models import signals
from datetime import date
from django.template.defaultfilters import slugify
from accounts.models import Patient


class RegisterManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(Register__icontains=query) | \
            models.Q(description__icontains=query)

)
class Register(models.Model):

    register_code = models.CharField('Código do Registro', max_length=100, null=False, unique=True, primary_key=True)
    register_type = models.CharField('Tipo do Registro', max_length = 100)
    hospital = models.CharField('Hospital', max_length= 50)
    slug = models.SlugField('Atalho', max_length = 150, editable=True)
    date_register = models.DateField('Data do Registro', null = True)
    about = models.TextField('Mais informações', blank = True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    consult = models.ForeignKey("consult.Consult", verbose_name='Consulta',
    related_name='consult_Register'
    )

    def __str__(self):
        return self.Register_code

    def save(self, *args, **kwargs):
        self.slug = slugify(self.register_code)
        super(Register, self).save(*args, **kwargs)

    def set_ativo(self):
        self.status = 0
        self.save()

    def set_encerrado(self):
        self.status = 1
        self.save()

    def set_declassificado(self):
        self.status = 2
        self.save()

    def set_arquivado(self):
        self.status = 3
        self.save()

    def is_ativo(self):
        return self.status == 0

    def is_encerrado(self):
        return self.status == 1

    def is_desclassificado(self):
        return self.status == 2

    def is_arquivado(self):
        return self.status == 3

    @models.permalink
    def get_absolute_url(self):
        return('register:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ['register_type']

class Consult_Register(models.Model):

    STATUS_CHOICES = (
    (0, 'Realizada'),
    (1, 'Pendente'),
    (2, 'Cancelada'),
    (3, 'Arquivada'),
    )

    consult = models.ForeignKey("consult.Consult", verbose_name='Consulta',
        related_name='consult_Consult_Register'
    )
    register = models.ForeignKey(
        Register, verbose_name='Registro', related_name='consult_register'
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=1, blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.consult + "->" + self.register

    def set_pending(self):
        self.status = 0
        self.save()

    def set_active(self):
        self.status = 1
        self.save()

    def set_closed(self):
        self.status = 2
        self.save()

    def is_pending(self):
        return self.status == 0

    def is_approved(self):
        return self.status == 1

    def is_closed(self):
        return self.status == 2

    def __str__(self):
        return str(self.consult) + " -> criou a Registro : " + str(self.register)

    class Meta:
        verbose_name = 'Médico_Registro'
        verbose_name_plural = 'Médicos_Registros'
        unique_together = (('consult', 'register'),)


