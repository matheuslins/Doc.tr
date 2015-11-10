from django.db import models
from django.conf import settings
from django.db.models import signals
from datetime import date
from django.template.defaultfilters import slugify
from accounts.models import Patient


class ConsultManager(models.Manager):

	def search(self,query):

		return self.get_queryset().filter(
		models.Q(consult__icontains=query) | \
		models.Q(description__icontains=query)

		)
class Consult(models.Model):

    consult_code = models.CharField('Código da Consulta', max_length=100, null=False, unique=True, primary_key=True)
    consult_type = models.CharField('Tipo de Consulta', max_length = 100)
    hospital = models.CharField('Hospital', max_length= 50)
    slug = models.SlugField('Atalho', max_length = 150, editable=True)
    date_consult = models.DateField('Data da Consulta', null = True)
    about = models.TextField('Mais informações', blank = True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    patient = models.ForeignKey(
        Patient, verbose_name='Paciente',
        related_name='consult_paciente',blank = True, null=True
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Médico',
        related_name='consult_médico'
    )

    def __str__(self):
        return self.consult_code

    def save(self, *args, **kwargs):
        self.slug = slugify(self.consult_code)
        super(Consult, self).save(*args, **kwargs)

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
        return('consult:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['consult_type']

class Doctor_consult(models.Model):

    STATUS_CHOICES = (
        (0, 'Realizada'),
        (1, 'Pendente'),
        (2, 'Cancelada'),
        (3, 'Arquivada'),
    )

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Médico',
        related_name='doctor_consult'
    )
    consult = models.ForeignKey(
        Consult, verbose_name='Consulta', related_name='doctor_consult'
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=1, blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.doctor + "->" + self.consult

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
        return str(self.doctor) + " -> criou a consulta : " + str(self.consult)

    class Meta:
        verbose_name = 'Médico_Consulta'
        verbose_name_plural = 'Médicos_Consultas'
        unique_together = (('doctor', 'consult'),)


