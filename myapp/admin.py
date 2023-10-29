# admin.py

from django.contrib import admin
from myapp.models import Departamento, Municipio, Comuna, Barrio
from myapp.models import Candidato, Registro
from myapp.models import PuestoVotacion, Mesa
from datetime import date, timedelta


# locations
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('name',)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'municipio')
    list_filter = ('municipio__departamento', 'municipio',)
    search_fields = ('name',)


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'municipio')
    list_filter = ('municipio',)
    search_fields = ('name',)

class MesaInline(admin.StackedInline):
    model = Mesa
    extra = 0


# Puesto Votacion y User
class PuestoVotacionAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'municipio', 'nombre', 'direccion', 'latitude', 'longitude', 'link')
    search_fields = ('nombre', 'direccion')
    list_filter = ('departamento', 'municipio')
    inlines = [MesaInline,]

class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'puesto_votacion')
    search_fields = ('numero', 'puesto_votacion')
    list_filter = ('numero', 'puesto_votacion')


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'partido', 'numero')
    search_fields = ('nombre', 'partido', 'numero')


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidato', 'mesa', 'numero_de_votos')
    search_fields = ('candidato', 'mesa', )


# locations
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Barrio, BarrioAdmin)

# Puesto Votacion y User
admin.site.register(PuestoVotacion, PuestoVotacionAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Registro, RegistroAdmin)

