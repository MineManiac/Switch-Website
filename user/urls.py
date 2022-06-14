from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='news'),
    path('api/news', views.api_news),
    path('api/signup', views.api_signup),
    path('api/user', views.api_user),
    path('api/login', views.api_get_token),
    path('send_friend_request',
        views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:request_id>',
        views.accept_friend_request, name='accept friend request'),
    path('deny_friend_request/<int:request_id>',
        views.deny_friend_request, name='deny friend request'),
]