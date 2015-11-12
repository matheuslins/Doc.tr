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
def creat_register_consult(request):

	template_name = 'creat_register_consult.html'
	form = RegisterForm(request.POST, request.FILES)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = request.user
			newform.save()
			slug = newform.slug
			register = get_object_or_404(Register, slug = slug)
			user = request.user
			vinculo, created = Consult_Register.objects.get_or_create(consult = consult, register = register)
			messages.success(request,'Registro criada com sucesso!')
			form = RegisterForm()
	else:
		form = RegisterForm()
	contexto['form'] = form
	return render(request, template_name,contexto)

@login_required(redirect_field_name='login_obrigatorio')
def registers(request):
	registers = Register.objects.all()
	template_name = 'registers.html'
	contexto = {
		'registers':registers
	}
	return render(request, template_name, contexto)

@login_required(redirect_field_name='login_obrigatorio')
def consult_register(request):
	consult_register = Consult_Register.objects.all()
	template_name = 'consult_register.html'
	contexto = {
		'consult_register':consult_register
	}
	return render(request, template_name, contexto)




