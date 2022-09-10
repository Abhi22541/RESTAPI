from django.urls import path
from . import views

urlpatterns = [
     path('', views.FilmOverview, name='home'),
     path('create/', views.add_film, name='add-film'),
     path('all/', views.view_film, name='view_film'),
     path('update/<int:pk>/', views.update_film, name='update-film'),
     path('film/<int:pk>/delete/', views.delete_film, name='delete-film')

]