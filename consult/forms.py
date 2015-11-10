# -*- coding: utf8 -*-
from django import forms
from .models import *
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify
from accounts.models import *
import datetime
import DocTr.settings

class ConsultForm(forms.ModelForm):

	class Meta:
		model = Consult
		fields = ['consult_code','consult_type','hospital','date_consult', 'about','patient','doctor']

# class Edit_EventoForm(forms.ModelForm):

# 	def evento_pre_save(signal, instance, sender, **kwargs):
# 		instance.slug = slugify(instance.name)
# 	signals.pre_save.connect(evento_pre_save, sender = Evento)

# 	def clean_valor(self):
# 		valor = self.cleaned_data['valor']
# 		if valor <= 0:
# 			raise forms.ValidationError('O valor não pode ser menor ou igual a zero')
# 		return  valor
# 	class Meta:
# 		model = Evento
# 		fields = ['name', 'place_event','date_event','date_event_finsh','start_date_errolment',
# 			'finsh_date_enrrolment','image','about','valor', 'pares']