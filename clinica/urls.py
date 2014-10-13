from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'clinicadental.views.home', name='home'),
    url(r'^tratamientos/$','clinicadental.views.tratamientos', name='tratamientos'),
    url(r'^contactanos/$','clinicadental.views.contactanos', name='contactanos'),
    url(r'^pidetucita/$','clinicadental.views.pidetucita', name='pidetucita'),
    url(r'^direccion/$','clinicadental.views.direccion', name='direccion'),
    url(r'^chat/$','clinicadental.views.chat', name='chat'),
    url(r'^mail/$','clinicadental.views.mail', name='mail'),

    # url(r'^map/$', 'clinicadental.views.map', name='map'),
    # url(r'^map1/$', 'clinicadental.views.map1', name='map1'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
