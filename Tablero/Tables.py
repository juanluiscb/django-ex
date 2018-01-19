import django_tables2 as tables
from django.utils.html import format_html

from Tablero.models import GrupoEquipos,Encuentro
from Tablero.Columns import *

class TBLGrupoEquipos(tables.Table):
    btnVerEncuentros = tables.Column(verbose_name="Encuentros")

    class Meta:
        model = GrupoEquipos
        attrs = {'class': 'table table-responsive'}
        fields = {'equipo','grupo','btnVerEncuentros'}
        sequence = ('equipo','grupo','btnVerEncuentros')


class TBLEncuentroPorEquipo(tables.Table):
    id = VsCol(verbose_name="Contra")
    class Meta:
        model = Encuentro
        attrs = {'class': 'table table-responsive'}
        fields = {'equipo1','equipo2','fecha_encuentro','estadio'}
        sequence = ('equipo1','id','equipo2','fecha_encuentro','estadio')