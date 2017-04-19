from django.conf.urls import url # importe les methods dont on a besoin
from . import views		# importe toutes les vues liées à notre app blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
