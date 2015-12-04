# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from accounts.models import *
from consult.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.contrib.auth import get_user
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
def creat_register_consult_exams(request,slug):
	
	template_name = 'creat_register_consult_exams.html'
	consult = get_object_or_404(Consult, slug = slug)
	form = RegisterFormExams(request.POST, request.FILES)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = request.user
			newform.consult = consult
			newform.register_code = newform.register_code + 1
			newform.save()
			messages.success(request,'Exame criado com sucesso!')
			form = RegisterFormExams()
	else:
		print('Não')
		form = RegisterFormExams()
	contexto['form'] = form
	contexto['hospital'] = consult.hospital
	contexto['doctor'] = consult.doctor
	contexto['patient'] = consult.patient
	contexto['consult'] = consult
	contexto['slug'] = slug
	return render(request, template_name,contexto)

@login_required(redirect_field_name='login_obrigatorio')
def creat_register_consult_treatments(request,slug):

	template_name = 'creat_register_consult_treatments.html'
	consult = get_object_or_404(Consult, slug = slug)
	form = RegisterFormTreatments(request.POST, request.FILES)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = request.user
			newform.consult = consult
			newform.register_code = newform.register_code + 1
			newform.save()
			messages.success(request,'Tratamento criado com sucesso!')
			form = RegisterFormTreatments()
	else:
		print('Não')
		form = RegisterFormTreatments()
	contexto['form'] = form
	contexto['hospital'] = consult.hospital
	contexto['doctor'] = consult.doctor
	contexto['patient'] = consult.patient
	contexto['consult'] = consult
	contexto['slug'] = slug
	return render(request, template_name,contexto)

@login_required(redirect_field_name='login_obrigatorio')
def registers(request):
	template_name = ''
	contexto = {}
	consults = None
	try:
		doctor = Doctor.objects.get(id = request.user.id)
		registers = Register.objects.all()
		template_name = 'registers.html'
	except Exception as e:
		patient = Patient.objects.get(id = request.user.id)
		registers = Doctor_consult.objects.all().filter(patient = patient)
		print('Paciente Registro')
		template_name = 'register_patient.html'
	contexto = {
		'registers':registers
	}
	return render(request, template_name, contexto)

@login_required(redirect_field_name='login_obrigatorio')
def consult_register(request):
	consult_register = Register.objects.all()
	template_name = 'consult_register.html'
	contexto = {
		'consult_register':consult_register
	}
	return render(request, template_name, contexto)

@login_required(redirect_field_name='login_obrigatorio')
def details_register(request, slug):
    template_name = 'details_register.html'
    context = {
    	'slug': slug
    }
    return render(request, template_name,context)

@login_required(redirect_field_name='login_obrigatorio')
def choice_register(request, slug):
    template_name = 'choice_register.html'
    context = {
    	'slug': slug
    }
    return render(request, template_name,context)

@login_required(redirect_field_name='login_obrigatorio')
def exams(request, slug):
    template_name = 'exams.html'
    exams = Exams.objects.all()
    context = {
    	'exams':exams,
    	'slug':slug
    }
    return render(request, template_name,context)
@login_required(redirect_field_name='login_obrigatorio')
def treatments(request, slug):
    template_name = 'treatments.html'
    treatments = Treatment.objects.all()
    context = {
    	'treatments':treatments,
    	'slug':slug
    }
    return render(request, template_name,context)

@login_required(redirect_field_name='login_obrigatorio')
def details_treatments(request, slug):
	template_name = 'details_treatments.html'
	treatments = get_object_or_404(Treatment,slug = slug)
	context = {
		'slug': slug,
		'treatment': treatments
	}
	return render(request, template_name,context)

@login_required(redirect_field_name='login_obrigatorio')
def details_exams(request, slug):

	exams = get_object_or_404(Exams,slug = slug)
	template_name = 'details_exams.html'
	context = {
		'slug': slug,
		'exam':exams
	}
	return render(request, template_name,context)






