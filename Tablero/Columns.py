import django_tables2 as tables
from django.utils.html import format_html


class VsCol(tables.Column):
    def render(self, value):
        return "Vs"