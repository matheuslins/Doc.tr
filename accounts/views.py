from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import EditAccountForm_Doctor
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from .forms import * 
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.template import Context, loader
from .models import *
from core.utils import generate_hash_key
from datetime import date
import datetime

User = get_user_model()

@login_required(redirect_field_name='login_obrigatorio')
def dashboard(request):
	template_name = 'dashboard.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def profile(request):
	template_name = 'profile.html'
	return render(request,template_name)

@login_required(redirect_field_name='login_obrigatorio')
def edit_profile(request):

	template_name = 'edit_profile.html'
	form = EditAccountForm_Doctor()
	contexto = {}
	if request.method == "POST":
		form = EditAccountForm_Doctor(request.POST, request.FILES, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Seus dados foram alterados com sucesso')
	else:
		form = EditAccountForm_Doctor(instance = request.user)
	contexto['form'] = form
	return render(request,template_name, contexto)

@login_required(redirect_field_name='login_obrigatorio')
def patients_list(request):
	template_name = 'patients_list.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def medication(request):
	template_name = 'medication.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def register(request):
	template_name = 'registors.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def edit_password(request):

	template_name = 'edit_password.html'
	contexto = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			MIN_LENGTH = 8
			password1 = form.cleaned_data['new_password1']

			# At least one letter and one non-letter
			first_isalpha = password1[0].isalpha()
			if all(c.isalpha() == first_isalpha for c in password1):
				messages.success(request,'A senha deve conter pelo menos uma letra e pelo menos um dígito ou "\
				"um caractere de pontuação.')
				form = PasswordChangeForm(data = request.POST, user = request.user)
			# At least MIN_LENGTH long
			elif len(password1) < MIN_LENGTH:
				messages.success(request,'A senha deve ter %d caracteres no mínimo.' % MIN_LENGTH)
				form = PasswordChangeForm(data = request.POST, user = request.user)
			else:
				form.save()
				contexto['success'] = True
				messages.success(request, 'Sua senha foi alterada com sucesso!')
	else:
		form = PasswordChangeForm(user = request.user)
	contexto['form'] = form
	return render(request, template_name,contexto)


'''
	Método para resetar a senha, para quando um usuário ainda NÃO logado esquece a senha.
'''
def password_reset(request):
	template_name = 'password_reset.html'
	contexto = {}
	form = PasswordResetForm(request.POST or None)

	if form.is_valid():
		form.save()
		contexto['success'] = True
		messages.success(request,'Um e-mail foi enviando para você, verifique sua caixa de entrada')
	contexto['form'] = form

	return render(request, template_name, contexto)

'''
	Antes de entrar nesse método, um email é enviado para o usuário e ele recebe um link que redireciona
	para esse método, que é o método que vai gerar uma nova senha para o usuário.

'''
def password_reset_confirm(request, key):
	template_name = 'password_reset_confirm.html'
	contexto = {}
	reset = get_object_or_404(PasswordReset, key = key)
	form = SetPasswordForm(user = reset.user, data = request.POST or None)
	if form.is_valid():
		MIN_LENGTH = 8
		password1 = form.cleaned_data['new_password1']

		# At least one letter and one non-letter
		first_isalpha = password1[0].isalpha()
		if all(c.isalpha() == first_isalpha for c in password1):
			messages.success(request,'A senha deve conter pelo menos uma letra e pelo menos um dígito ou "\
			"um caractere de pontuação.')
			form = SetPasswordForm(user = reset.user, data = request.POST)
		# At least MIN_LENGTH long
		elif len(password1) < MIN_LENGTH:
			messages.success(request,'A senha deve ter %d caracteres no mínimo.' % MIN_LENGTH)
			form = SetPasswordForm(user = reset.user, data = request.POST)
		else:
			form.save()
			contexto['success'] = True
			messages.success(request,'Sua senha foi criada com sucesso')
	contexto['form'] = form

	return render(request,template_name,contexto)


