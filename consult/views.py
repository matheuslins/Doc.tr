# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from accounts.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.contrib.auth import get_user
from register.models import *
import datetime
import copy
from .models import *
# SIGNALS AND LISTENERS
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import dispatcher
# EXTRAS
from datetime import date


@login_required(redirect_field_name='login_obrigatorio')
def create_consult(request):

	template_name = 'create_consult.html'
	form = ConsultForm(request.POST, request.FILES)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = request.user
			patient = newform.patient
			print('1')
			newform.consult.consult_id = newform.consult.consult_code
			print('2')
			newform.consult = request.POST['consult_code']
			print('3')
			newform.save()
			slug = newform.consult.slug
			consult = get_object_or_404(Consult, slug = slug)
			user = Doctor.objects.get(id=request.user.id)
			vinculo, created = Doctor_consult.objects.get_or_create(doctor = user, consult = consult, patient = patient)
			messages.success(request,'Consulta criada com sucesso!')
			form = ConsultForm()
	else:
		print('Não!')
		form = ConsultForm()
	contexto['form'] = form
	return render(request, template_name,contexto)


def consults(request):
	template_name = ''
	contexto = {}
	consults = None
	try:
		doctor = Doctor.objects.get(id = request.user.id)
		consults = Doctor_consult.objects.all().filter(doctor = doctor)
		template_name = 'consult.html'
	except Exception as e:
		patient = Patient.objects.get(id = request.user.id)
		consults = Doctor_consult.objects.all().filter(patient = patient)
		template_name = 'consult_patient.html'
	contexto['consults'] = consults
	return render(request, template_name, contexto)


def details_consult(request, slug):
	template_name = ''
	context = {}
	# try:
	doctor = Doctor.objects.get(id = request.user.id)
	consult = get_object_or_404(Consult, slug = slug)
	treatment = Treatment.objects.all().filter(consult__consult = consult)
	exam = Exams.objects.all().filter(consult__consult = consult)
	print(treatment)
	template_name = 'details_consult.html'
	# except Exception as e:
	# 	patient = Patient.objects.get(id = request.user.id)
	# 	consults = Doctor_consult.objects.all().filter(patient = patient)
	# 	template_name = 'details_consult.html'
	context['slug'] = slug
	context['treatments'] = treatment
	context['exams'] = exam
	return render(request, template_name,context)













