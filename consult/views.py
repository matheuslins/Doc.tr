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
def create_consult(request):

	template_name = 'create_consult.html'
	form = ConsultForm(request.POST, request.FILES)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = request.user
			now = datetime.datetime.now().date()
			newform.save()
			slug = newform.slug
			consult = get_object_or_404(Consult, slug = slug)
			user = request.user
			vinculo, created = Doctor_consult.objects.get_or_create(doctor = user, consult = consult)
			messages.success(request,'Consulta criada com sucesso!')
			form = ConsultForm()
	else:
		form = ConsultForm()
	contexto['form'] = form
	return render(request, template_name,contexto)

