# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html

CHOISE_CONTINENTE = (
    ('AMERICA', 'AMERICA'),
    ('ASIA', 'ASIA'),
    ('AFRICA', 'AFRICA'),
    ('EUROPA', 'EUROPA'),
    ('OCEANIA', 'OCEANIA'),
)

CHOISE_FASES = (
    ('GRUPOS', 'GRUPOS'),
    ('OCTAVOS DE FINAL', 'OCTAVOS DE FINAL'),
    ('CUARTOS DE FINAL', 'CUARTOS DE FINAL'),
    ('SEMIFINAL', 'SEMIFINAL'),
    ('TERCER PUESTO', 'TERCER PUESTO'),
    ('FINAL', 'FINAL'),
)


class Equipo(models.Model):
    nombre = models.CharField(max_length=150, blank=False, help_text="Nombre del Equipo")
    continente = models.CharField(choices=CHOISE_CONTINENTE, max_length=50, default='AMERICA')
    bandera = models.FileField(upload_to='banderas/', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class Grupo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=80, help_text='Descripcion del Grupo')

    def __str__(self):
        return self.descripcion

class GrupoEquipos(models.Model):
    equipo = models.ForeignKey('Equipo')
    grupo = models.ForeignKey('Grupo')
    posicion = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.equipo,self.grupo)

    def btnVerEncuentros(self):
        return format_html(
            '<a href="/encuentros-equipo/?equipo_id={}">Ver Encuentros</a>', self.equipo.id
        )

class Estadio(models.Model):
    nombre_estadio = models.CharField(max_length=250)
    localidad = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nombre_estadio

    class Meta:
        verbose_name = 'Estadio'
        verbose_name_plural = 'Estadios'


class Encuentro(models.Model):
    equipo1 = models.ForeignKey('Equipo', related_name='Equipo1',verbose_name="Equipo1")
    equipo2 = models.ForeignKey('Equipo', related_name='Equipo2',verbose_name="Equipo2")
    estadio = models.ForeignKey('Estadio')
    gol_equipo1 = models.IntegerField(default=0)
    gol_equipo2 = models.IntegerField(default=0)
    finalizado = models.BooleanField(default=False)
    fecha_encuentro = models.DateTimeField(auto_now=False)
    fase = models.CharField(choices=CHOISE_FASES, max_length=80,default='GRUPOS')
    tiempo_regular = models.BooleanField(default=True)
    tiempo_extra = models.BooleanField(default=False)
    gol_oro = models.BooleanField(default=False)
    penales = models.BooleanField(default=False)

    def __str__(self):
        return "( {} ) {} vs {} ( {} )".format(self.gol_equipo1, self.equipo1, self.equipo2, self.gol_equipo2)

    class Meta:
        verbose_name = 'Encuentro'
        verbose_name_plural = 'Encuentros'

    def ActualizaTablaGeneral(self):
        if self.gol_equipo1 == self.gol_equipo2:
            eq1 = TablaGeneral.objects.get(equipo=self.equipo1)
            eq2 = TablaGeneral.objects.get(equipo=self.equipo2)
            eq1.Empate(self.gol_equipo1)
            eq2.Empate(self.gol_equipo2)
        elif self.gol_equipo1 > self.gol_equipo2:
            eq1 = TablaGeneral.objects.get(equipo=self.equipo1)
            eq2 = TablaGeneral.objects.get(equipo=self.equipo2)
            eq1.Gane(self.gol_equipo1, self.gol_equipo2)
            eq2.Pierde(self.gol_equipo2, self.gol_equipo1)
        else:
            eq1 = TablaGeneral.objects.get(equipo=self.equipo1)
            eq2 = TablaGeneral.objects.get(equipo=self.equipo2)
            eq1.Pierde(self.gol_equipo1, self.gol_equipo2)
            eq2.Gane(self.gol_equipo2, self.gol_equipo1)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):

        if self.finalizado:
            self.ActualizaTablaGeneral()

        super(Encuentro, self).save(*args, **kwargs)


class TablaGeneral(models.Model):
    equipo = models.ForeignKey('Equipo')
    puntos = models.IntegerField(default=0)
    pj = models.IntegerField(default=0, help_text='Partidos Jugados', verbose_name='PJ')
    pg = models.IntegerField(default=0, help_text='Partidos Ganados', verbose_name='PG')
    pe = models.IntegerField(default=0, help_text='Partidos Empatados', verbose_name='PE')
    pp = models.IntegerField(default=0, help_text='Partidos Perdidos', verbose_name='PP')
    gf = models.IntegerField(default=0, help_text='Goles a Favor', verbose_name='GF')
    gc = models.IntegerField(default=0, help_text='Goles en Contra', verbose_name='GC')
    dif = models.IntegerField(default=0, help_text='Diferencia', verbose_name='DIF')

    def __str__(self):
        return "{} {}".format(self.equipo, self.puntos)

    class Meta:
        verbose_name = 'Tabla General'
        verbose_name_plural = 'Tabla General'

    def Empate(self, numgol):
        self.puntos += 1
        self.pj += 1
        self.pe += 1
        self.gf += numgol
        self.gc += numgol
        self.dif = self.gf - self.gc
        self.save()

    def Gane(self, gf, gc):
        self.puntos += 3
        self.pj += 1
        self.pg += 1
        self.gf += gf
        self.gc += gc
        self.dif = self.gf - self.gc
        self.save()

    def Pierde(self, gf, gc):
        self.pj += 1
        self.pp += 1
        self.gf += gf
        self.gc += gc
        self.dif = self.gf - self.gc
        self.save()

    def GetPosicionGeneral(self):
        pass

    def GetPosicionGrupo(self):
        pass

class Quiniela(Encuentro):
    jugador = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now=True)