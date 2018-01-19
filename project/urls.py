from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

# from welcome.views import index, health
from Tablero.views import index,ListaEquipos

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='inicio'),
    # url(r'^health$', health),
    url(r'^equipos/', ListaEquipos, name='equipos'),
    url(r'^admin/', include(admin.site.urls,)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
