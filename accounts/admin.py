from django.contrib import admin
from accounts.models import UserU
from accounts.models import Doctor,Patient

admin.site.register(UserU)
admin.site.register(Doctor)
admin.site.register(Patient)
