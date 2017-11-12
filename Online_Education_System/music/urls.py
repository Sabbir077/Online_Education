from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
   # url(r'^album(?p<album_id>[0-9]+)$', views.album,name='album'),
    url(r'^song$', views.song,name='song'),
     url(r'^album$', views.album,name='album'),
     url(r'^(?P<album_id>[0-9]+)/$', views.detail,name='detail'),
     url(r'^sabbir$', views.sabbir ,name='sabbir'),

]

