from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^modes/$', views.modes, name='modes'),
    url(r'^scales/$', views.scales, name='scales'),
    url(r'^intervals/$', views.intervals, name='intervals'),
    url(r'^scale/$', views.get_scale, name='get_scale'),
]