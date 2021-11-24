from django.urls.conf import path, re_path
from . import views
from django.conf.urls import url

app_name = 'store'

urlpatterns = [
    #path('', views.index, name='home')
    path('', views.listing, name='listing'),
    re_path(r'^(?P<album_id>[0-9])', views.detail,name='detail'),
    path('search/', views.search, name='search'),
]

