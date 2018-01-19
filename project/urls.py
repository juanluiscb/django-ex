from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import health
from Tablero.views import index,ListaEquipos,ListaEncuentroPorEquipo,Acercade

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='inicio'),
    url(r'^health$', health),
    url(r'^equipos/', ListaEquipos, name='equipos'),
    url(r'^encuentros-equipo/', ListaEncuentroPorEquipo,name='encuentros-equipo'),
    url(r'^admin/', include(admin.site.urls,)),
    url(r'^acercade/', Acercade,name='acercade'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
