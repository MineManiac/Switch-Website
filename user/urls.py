from django.urls import path

from . import views

urlpatterns = [
    path('', views, name='index'),
    path('api/user/<int:user_id>/', views.api_user),
    # Você possivelmente tem outras rotas aqui.
]