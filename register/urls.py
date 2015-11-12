from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [
    url(r'^$', 'register.views.registers', name='registers'),
     url(r'^criar_registro_consulta', 'register.views.creat_register_consult', name='creat_register_consult'),
    url(r'^registros_da_consulta', 'register.views.consult_register', name='consult_register'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
