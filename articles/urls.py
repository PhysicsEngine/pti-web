from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author, name='author'),
]
