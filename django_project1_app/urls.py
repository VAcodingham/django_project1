from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:someint>', views.show),
    path('<int:someint>/edit', views.edit),
    path('<int:someint>/delete', views.destroy)
]