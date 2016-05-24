from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.smilesSearch, name='smiles_search'),
    # url(r'^result$',views.result, name = 'search_result'),
    url(r'^result/(?P<pk>[0-9]+)/$', views.result, name='search_result'),
    url(r'^ketcher$',views.ketcher, name = 'ketcher'),
    url(r'^image_search$',views.imageSearch, name = 'image_search'),
    url(r'^file_upload$',views.fileSearch, name = 'file_search'),
]