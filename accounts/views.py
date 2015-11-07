from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login_obrigatorio')
def dashboard(request):
	template_name = 'dashboard.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def profile(request):
	template_name = 'profile.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def patients_list(request):
	template_name = 'patients_list.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def consult(request):
	template_name = 'consult.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def medication(request):
	template_name = 'medication.html'
	return render(request, template_name)

@login_required(redirect_field_name='login_obrigatorio')
def register(request):
	template_name = 'registors.html'
	return render(request, template_name)