from django.contrib import admin
from .models import *

class ConsultAdmin(admin.ModelAdmin):
	list_display = ['consult_code','created_at'] # modifica a forma que o admin mostra os objetos
	search_fields = ['consult_code', 'consult_code'] # cria uma barra de pesquisa
	prepopulated_fields = {'slug': ('consult_code',)} 

admin.site.register(Consult, ConsultAdmin)
admin.site.register(Doctor_consult)
