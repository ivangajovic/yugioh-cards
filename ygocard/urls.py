from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.card_list, name='card_list'),
    url(r'^card/(?P<pk>\d+)/$', views.card_detail, name='card_detail'),
    url(r'^card/new/$', views.add_new_card, name='add_new_card'),
    url(r'^card/(?P<pk>\d+)/edit/$', views.card_edit, name='card_edit'),
    url(r'^card/(?P<pk>\d+)/remove/$', views.card_remove, name='card_remove'),
    url(r'^signup/$', views.signup, name='signup'),
]
