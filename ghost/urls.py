from django.urls import path

from . import views

app_name = 'ghost'
urlpatterns = [
    path('', views.index, name='index'),
    path('ghost_worker', views.ghost_worker, name='ghost_worker')
]
