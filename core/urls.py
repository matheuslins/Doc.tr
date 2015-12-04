from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [
    
    url(r'^$', 'core.views.home', name='home'),
    url(r'^rest', 'core.views.rest', name='rest'),
    url(r'^cadastrar_medico', 'core.views.register_doctor', name='register_doctor'),
    url(r'^cadastrar_pacitente', 'core.views.register_patient', name='register_patient'),
    url(r'^escolha_cadastro', 'core.views.choice_register', name='choice_register'),
    url(r'^login', 'django.contrib.auth.views.login',{'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout',{'next_page': 'core:login'}, name='logout'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='{{STATIC_URL}}/assets/img/icon.png'))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
