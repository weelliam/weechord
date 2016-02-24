from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^chordbuilder/', include('chordbuilder.urls')),
    url(r'^admin/', admin.site.urls),
]
