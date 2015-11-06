from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from perfil.views import HombresList
from perfil.views import HombresDetailList
from perfil.views import MujeresDetailList
from perfil.views import MujeresList


from django.contrib.auth import views as auth_views

from perfil import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/', views.inicio, name='inicio'),
    url(r'^pais/', views.pais, name='pais'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^rango/', views.inicio, name='inicio'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^talentos_h/', views.HombresList.as_view()),
    url(r'^talentos_m/', views.MujeresList.as_view()),
    url(r'^search/', include('haystack.urls')),
    url(r'^(?P<slug>[-\w]+)/$', HombresDetailList.as_view(), name='Detalle-Hombres'),
    url(r'^(?P<slug>[-\w]+)/$', MujeresDetailList.as_view(), name='Detalle-Hombres'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'TheGlobalCasting Admin'


# script cambio de edades#