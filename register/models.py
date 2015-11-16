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

    register_code = models.IntegerField('ID',primary_key=True, null=False, blank=False)
    about = models.TextField('Mais informações', blank = True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    slug = models.SlugField('Atalho', max_length = 150, editable=True)

    consult = models.ForeignKey("consult.Consult", verbose_name='Consulta',
        related_name='register_Consult'
    )

    def __str__(self):
        return self.register_code

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
        return('register:details_register', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ['register_code']

class Exams(Register):

    result = models.TextField('Resultado do Exame', max_length= 50,null=True,blank=True)

    def __str__(self):
        return "Exame -> " + self.result or "Exame -> padrão"

    def get_short_name(self):
        return self.result

    def get_full_name(self):
        return str(self)

    @models.permalink
    def get_absolute_url(self):
        return('register:details_exams', (), {'slug': self.slug})


    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

class Medicine(models.Model):

    name = models.CharField('Nome do medicamento', max_length= 50,null=False, primary_key=True)

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'


class Treatment(Register):

    medicine = models.ManyToManyField(Medicine, verbose_name='Medicamento',
        related_name='medicine_Treatment', blank=True
    )

    def __str__(self):
        return "Tratamento -> " + self.about or "Tratamento -> padrão"

    def get_short_name(self):
        return self.about

    def get_full_name(self):
        return str(self)

    @models.permalink
    def get_absolute_url(self):
        return('register:details_treatments', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Tratamento'
        verbose_name_plural = 'Tratamentos'



