from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',...)

urlpatterns = [
    
    url(r'^$', 'core.views.home', name='home'),
    url(r'^cadastrar', 'core.views.register', name='register'),
    url(r'^login', 'django.contrib.auth.views.login',{'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout',{'next_page': 'core:login'}, name='logout'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='{{STATIC_URL}}/assets/img/icon.png'))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
