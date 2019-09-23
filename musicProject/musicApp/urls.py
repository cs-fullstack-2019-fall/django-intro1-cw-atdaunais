from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('music/', views.music),
    path('brockhampton/', views.brockhampton),
    path('jacobCollier/', views.jacobCollier),
    path('activeChild/', views.activeChild),
}