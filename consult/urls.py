from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [

    url(r'^$', 'consult.views.consults', name='consults'),
    url(r'^criar_consulta', 'consult.views.create_consult', name='create_consult'),
    url(r'^(?P<slug>[\w_-]+)/consulta_detalhe', 'consult.views.details_consult', name='details_consult'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
