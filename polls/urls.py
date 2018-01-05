from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.getOne),
    path('create', views.create),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update)
]
