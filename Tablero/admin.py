# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Tablero.models import Equipo,Grupo,GrupoEquipos,Estadio,Encuentro,\
    TablaGeneral,Quiniela

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre','continente',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Equipo,EquipoAdmin)


class GrupoEquipoInLine(admin.TabularInline):
    model = GrupoEquipos
    extra = 0

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    inlines = [GrupoEquipoInLine,]
    ordering = ('nombre',)

admin.site.register(Grupo,GrupoAdmin)

class EstadioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estadio,EstadioAdmin)

class EncuentroAdmin(admin.ModelAdmin):
    list_display = ('equipo1','gol_equipo1','equipo2','gol_equipo2','finalizado','fecha_encuentro','estadio',)
    list_display_links = ('equipo1','equipo2','fecha_encuentro','estadio',)
    list_editable = ('gol_equipo1','gol_equipo2','finalizado')
    list_filter = ('equipo1','equipo2',)
    search_fields = ('equipo1__nombre','equipo2__nombre',)
    ordering = ('fecha_encuentro',)

admin.site.register(Encuentro,EncuentroAdmin)

class TablaGeneralAdmin(admin.ModelAdmin):
    list_display = ('equipo','puntos','pj','pg','pe','pp','gf','gc','dif',)
    ordering = ('-puntos','-dif','equipo','pj',)


admin.site.register(TablaGeneral,TablaGeneralAdmin)

class QuinielaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quiniela,QuinielaAdmin)