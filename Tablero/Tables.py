import django_tables2 as tables
from django.utils.html import format_html

from Tablero.models import GrupoEquipos

class TBLGrupoEquipos(tables.Table):

    class Meta:
        model = GrupoEquipos
        attrs = {'class': 'table table-responsive'}
        fields = {'equipo','grupo'}
        sequence = ('equipo','grupo',)