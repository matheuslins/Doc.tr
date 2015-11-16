from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [
    url(r'^$', 'register.views.registers', name='registers'),
    url(r'^criar_exames_consulta(?P<slug>[\w_-]+)', 'register.views.creat_register_consult_exams', name='creat_register_consult_exams'),
    url(r'^criar_tratamento_consulta(?P<slug>[\w_-]+)', 'register.views.creat_register_consult_treatments', name='creat_register_consult_treatments'),
    url(r'^(?P<slug>[\w_-]+)/escolha_registro', 'register.views.choice_register', name='choice_register'),
   	url(r'^(?P<slug>[\w_-]+)/exames', 'register.views.exams', name='exams'),
   	url(r'^(?P<slug>[\w_-]+)/tratamentos', 'register.views.treatments', name='treatments'),
    url(r'^registros_da_consulta', 'register.views.consult_register', name='consult_register'),
    url(r'^(?P<slug>[\w_-]+)/registro_detalhe', 'register.views.details_register', name='details_register'),
    url(r'^(?P<slug>[\w_-]+)/exame_detalhe', 'register.views.details_exams', name='details_exams'),
    url(r'^(?P<slug>[\w_-]+)/tratamento_detalhe', 'register.views.details_treatments', name='details_treatments'),



]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
