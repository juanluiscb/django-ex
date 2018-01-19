# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.context_processors import csrf

from Tablero.Tables import TBLGrupoEquipos, TBLEncuentroPorEquipo
from Tablero.models import GrupoEquipos, Encuentro,Equipo

title = ":: Mundialito Rusia 2018"
titulo = ":: Mundialito Rusia 2018"
contexto = {
    'title': title,
    'titulo': titulo
}


def index(request):
    return render(request, 'base.html', contexto)


def ListaEquipos(request):
    tblGruposEquipos = TBLGrupoEquipos(GrupoEquipos.objects.all().order_by('grupo__nombre', 'equipo__nombre'))

    contexto['tabla'] = tblGruposEquipos
    contexto.update(csrf(request))

    return render(request, 'tablero_lista_grupos_equipos.html', contexto)


def ListaEncuentroPorEquipo(request):
    if request.method == 'GET':
        equipo = Equipo.objects.filter(id = request.GET['equipo_id'])
        tblEncuentros = TBLEncuentroPorEquipo(Encuentro.objects.filter(equipo1=equipo) | Encuentro.objects.filter(equipo2=equipo))

        contexto['tblencuentros'] = tblEncuentros
        contexto.update(csrf(request))
        return render(request,'encuentros_por_equipo.html',contexto)
    else:
        return render(request,'base.html',contexto)

def Acercade(request):
    return render(request,'acercade.html',contexto)