from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [
    
    url(r'^$', 'accounts.views.dashboard', name='dashboard'),
    url(r'^seu_perfil', 'accounts.views.profile', name='profile'),
    url(r'^editar_perfil', 'accounts.views.edit_profile', name='edit_profile'),
    url(r'^lista_pacientes', 'accounts.views.patients_list', name='patients_list'),
    url(r'^medicamentos', 'accounts.views.medication', name='medication'),
    url(r'^registros', 'accounts.views.register', name='register'),
    url(r'^editar_senha/$', 'accounts.views.edit_password', name = 'edit_password'),


]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
