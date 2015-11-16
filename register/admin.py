from django.contrib import admin
from .models import *

class RegisterAdmin(admin.ModelAdmin):
	list_display = ['register_code','created_at'] # modifica a forma que o admin mostra os objetos
	prepopulated_fields = {'slug': ('register_code',)}

admin.site.register(Register, RegisterAdmin)
admin.site.register(Exams)
admin.site.register(Medicine)
admin.site.register(Treatment)
