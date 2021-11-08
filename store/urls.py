from django.urls.conf import path, re_path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('', views.index, name='home')
    path('', views.listing),
    re_path(r'^(?P<album_id>[0-9])', views.detail),
    path('search/', views.search),
]

