# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.

class Familia_Inline(admin.TabularInline):
	model = Familia
	max_num = 1
	can_delete = False

class Educacion_Inline(admin.TabularInline):
	model = Educacion
	extra = 1
	max_num = 9
	can_delete = True

class Tenencia_Propiedad_Inline(admin.TabularInline):
	model = Tenencia_Propiedad
	max_num = 1
	can_delete = False

class Uso_Tierra_Inline(admin.StackedInline):
	model = Uso_Tierra
	max_num = 1
	can_delete = False
	fieldsets = [
		('Área total en manzanas que tiene la propiedad',{'fields': ['area_total']}),
		('Número de manzanas en la que esta distribuida la finca', {'fields': [('bosque','tacotal','cultivo_anual'),
																				('plantacion_forestal','area_pasto_abierto','area_pasto_arboles'),
																				('cultivo_perenne','cultivo_semi_perenne','cacao'),
																				('huerto_mixto_cacao',)
			]}),
	]

class Reforestacion_Inline(admin.TabularInline):
	model = Reforestacion
	max_num = 1
	can_delete = False

class Caracterizacion_Terreno_Inline(admin.TabularInline):
	model = Caracterizacion_Terreno
	max_num = 1
	can_delete = False

class Fenomenos_Naturales_Inline(admin.TabularInline):
	model = Fenomenos_Naturales
	max_num = 1
	can_delete = False

class Razones_Agricolas_Inline(admin.TabularInline):
	model = Razones_Agricolas
	max_num = 1
	can_delete = False

class Razones_Mercado_Inline(admin.TabularInline):
	model = Razones_Mercado
	max_num = 1
	can_delete = False

class Inversion_Inline(admin.TabularInline):
	model = Inversion
	max_num = 1
	can_delete = False

class Mitigacion_Riesgos_Inline(admin.TabularInline):
	model = Mitigacion_Riesgos
	max_num = 1
	can_delete = False

class Organizacion_Asociada_Inline(admin.TabularInline):
	model = Organizacion_Asociada
	max_num = 1
	can_delete = False

class Area_Cacao_Inline(admin.TabularInline):
	model = Area_Cacao
	max_num = 1
	can_delete = False

class EncuestaAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		if request.user.is_superuser:
			return Encuesta.objects.all()
		return Encuesta.objects.filter(usuario=request.user)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

	exclude = ('usuario',)
	fieldsets = [
		(('Informacion Básica'), {'fields' : (('fecha','recolector','organizacion'),('nombre','cedula','fecha_nacimiento',)
			,('sexo','profesion','nombre_finca'),('departamento','municipio','comunidad'),('latitud','longitud')
			)}),
	]
	inlines = [Familia_Inline,Educacion_Inline,Tenencia_Propiedad_Inline,Uso_Tierra_Inline,Reforestacion_Inline,
				Caracterizacion_Terreno_Inline,Fenomenos_Naturales_Inline,Razones_Agricolas_Inline,Razones_Mercado_Inline,
				Inversion_Inline,Mitigacion_Riesgos_Inline,Organizacion_Asociada_Inline,Area_Cacao_Inline]
	list_display = ('nombre','organizacion','recolector','departamento','municipio')
	list_display_links = ('organizacion','nombre')
	list_filter = ('departamento',)
	class Media:
		css = {
            'all': ('admin.css',)
        }
	
admin.site.register(Encuesta,EncuestaAdmin)
admin.site.register(Organizaciones)
admin.site.register(Recolector)
admin.site.register(Situacion)
admin.site.register(Tipos_Servicio)
admin.site.register(Beneficios)