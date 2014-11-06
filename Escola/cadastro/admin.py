from django.contrib import admin
from models import cadastro

# Register your models here.

class Admin (models.modelAdmin):

	list_display = ['Nome','Endereco'] 
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']

class TipoUsuarioAdmin(Admin.modelAdmin)
	list_display = ['Tipo']
	search_fields= ['Tipo']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(TipoUsuario,TipoUsuarioAdmin)