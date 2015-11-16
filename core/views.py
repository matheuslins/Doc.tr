from django.shortcuts import render,redirect
from accounts.forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model

def home(request):
	template_name = 'index.html'
	return render(request, template_name)

def register(request):

	template_name = 'register.html'
	form = RegisterForm_Doctor(request.POST)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Seu cadastro foi feito com sucesso!')
			user = authenticate(username = user.username, password = form.cleaned_data['password1'])
			user.save()
			return redirect('accounts:dashboard')
	else:
		form = RegisterForm_Doctor()
	contexto['form'] = form
	return render(request, template_name, contexto)
