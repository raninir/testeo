from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^MascotaLista/$', views.MascotaApiShow.as_view()),
]