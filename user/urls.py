from django.urls import path

from . import views

urlpatterns = [
    path('', views.novidade_games, name='news'),
    path('api/news', views.api_news),
    path('api/user', views.api_user),
    path('send_friend_request/<int:userID>/',
        views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:userID>/',
        views.accept_friend_request, name='accept friend request'),
]