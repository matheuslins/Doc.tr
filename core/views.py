from django.shortcuts import render

def home(request):
	template_name = 'index.html'
	return render(request, template_name)

def register(request):
	template_name = 'register.html'
	return render(request, template_name)
