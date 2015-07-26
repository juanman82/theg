from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


from perfil import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/', views.inicio, name='inicio'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'TheGlobalCasting Admin'
