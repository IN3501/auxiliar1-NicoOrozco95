from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pestaña/', views.pestaña, name='pestaña'),
	path('integrantesdeequipodocente', views.integrantesdeequipodocente, name='integrantesdeequipodocente' ),
	path('cosasamicriterio', views.cosasamicriterio, name='cosasamicriterio'),
] 