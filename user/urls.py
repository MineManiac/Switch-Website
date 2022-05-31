from django.urls import path

from . import views

urlpatterns = [
    path('', views.novidade_games, name='news'),
    path('api/news', views.api_news),
    path('api/user', views.api_user),
    path('api/user/token', views.api_get_token),
    path('send_friend_request/<int:user_id>/',
        views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:user_id>/',
        views.accept_friend_request, name='accept friend request'),
]