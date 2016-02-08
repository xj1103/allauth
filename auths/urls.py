from django.conf.urls import patterns, url

from auths import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index')
)