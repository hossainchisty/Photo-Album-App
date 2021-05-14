from django.urls import path
from . import views

urlpatterns = [
    path('humanize-data/', views.Index, name="humanize"),
    path('',views.album, name="home"),
    path('photo/<int:pk>',views.photo, name="photo"),
    path('edit/<int:pk>',views.editPhoto, name="edit"),
    path('delete/<int:pk>',views.deletePhoto, name="delete"),

    path('add/',views.addPhoto, name="add"),
    path('query/',views.result, name="query"),
    path('profile/',views.profile, name="profile"),
]

