from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
   # url(r'^album(?p<album_id>[0-9]+)$', views.album,name='album'),
    url(r'^course/$', views.course,name='course'),
    url(r'^result/$', views.result,name='result'),

    url(r'^question/$', views.question,name='question'),
    url(r'^teacher/$', views.teacher,name='teacher'),
    url(r'^student/$', views.student,name='student'),
    url(r'^login/$', views.login,name='login'),
    url(r'^home/$', views.home,name='home'),
    url(r'^exam/$', views.exam,name='exam'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.exam_detail,name='exam_detail'),
    url(r'^signup/$', views.signup, name='signup'),

]
