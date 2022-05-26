from django.urls import path

from . import views

urlpatterns = [
    path('', views.novidade_games, name='news'),
    path('api/news', views.api_news),

]