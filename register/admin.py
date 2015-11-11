from django.contrib import admin
from .models import *

class RegisterAdmin(admin.ModelAdmin):
	list_display = ['register_code','date_register','created_at'] # modifica a forma que o admin mostra os objetos
	search_fields = ['register_code', 'register_code'] # cria uma barra de pesquisa
	prepopulated_fields = {'slug': ('register_code',)} 

admin.site.register(Register, RegisterAdmin)
admin.site.register(Consult_Register)