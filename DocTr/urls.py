
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^consultas/', include('consult.urls', namespace='consult')),
    url(r'^registros/', include('register.urls', namespace='register')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
