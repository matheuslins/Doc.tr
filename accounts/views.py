from django.shortcuts import render


def dashboard(request):
	template_name = 'dashboard.html'
	return render(request, template_name)

def profile(request):
	template_name = 'profile.html'
	return render(request, template_name)