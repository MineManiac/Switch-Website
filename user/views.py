from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from django.contrib.auth.models import User as User
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.http import Http404, HttpResponseForbidden, JsonResponse
from rest_framework.authtoken.models import Token

import user
from .models import Friend_Request, User
from .serializers import UserSerializer, FriendRequestsSerializer, UsernameSerializer, UserFriendsSerializer
import requests

def index(request):
    return HttpResponse("Olá mundo! Este é o caminho do vazio. Aqui é bem vazio, vá para http://localhost:8000/api/news lá é muito mais cheio")

@api_view(['GET'])
def api_news(request):

    url = "https://gaming-news.p.rapidapi.com/news"

    headers = {
	    "X-RapidAPI-Host": "gaming-news.p.rapidapi.com",
	    "X-RapidAPI-Key": "431b871e74msha3177211b2d7899p1645e3jsnde8a9570000a"
    }

    response = requests.request("GET", url, headers=headers)

    return HttpResponse(response.text)

@api_view(['POST'])
def api_signup(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            if username is not None and password is not None:
                if not User.objects.filter(username = username):
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.save()
                    return Response({"response":"User created successfully!"})
                else:
                    return Response({"response":"Username already exists. Please, try again."})      
    except:
        return HttpResponseForbidden()

@api_view(['POST'])
def api_get_token(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"token":token.key})
        else:
            return HttpResponseForbidden()

@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def send_friend_request(request):
    if request.method == 'POST':
        from_user = request.user
        # from_user = User.objects.get(id = 2)
        try:
            to_user = User.objects.all().filter(username=request.data["friendName"])[0]
        except:
            print("User not found")
            return Response({"response":"User not found!"})
        # to_user = User.objects.get(id=user_id)
        friend_request, created = Friend_Request.objects.get_or_create(
            from_user = from_user, to_user = to_user)
        if created:
            return Response({"response":"Friend Request Sent!"})
        else:
            return Response({"response":"Friend Request Already Sent!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accept_friend_request(request, request_id):
    friend_request = Friend_Request.objects.all().filter(id=request_id)[0]
    if friend_request.to_user == request.user:
        print(friend_request.from_user)
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.delete()
        print("Aceitou a request")
    
    return Response()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deny_friend_request(request, request_id):
    friend_request = Friend_Request.objects.all().filter(id=request_id)[0]
    friend_request.delete()
    print("Deletou a request")

    return Response()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user(request):
    this_user = request.user
    # this_user = User.objects.get(id = 3)
    all_users = User.objects.all()
    # Obtém as FriendRequests feitas ao usuário
    # friend_requests = Friend_Request.objects.all().filter(to_user=this_user)
    friend_requests = Friend_Request.objects.all().filter(to_user=this_user)
    # Serializa essas request
    serialized_frs = FriendRequestsSerializer(friend_requests, many = True)
    friend_requests_data = serialized_frs.data

    # A resposta devolvida ao FrontEnd da aplicação será um dicionário contendo: 
    # - uma lista de dicionários de usuários que fizeram Friend Request 
    # para este usuário e o devido ID da Request realizada;
    # - uma lista de amigos deste usuário.

    lista_frs = []
    # Para cada FR, pega o nome do usuário que fez a FR através de seu ID
    for fr in friend_requests_data:
        fr_user = all_users.filter(id=fr["from_user"])
        # Serializa Usuário para que seja retornado apenas uma string com seu Username
        serialized_username = UsernameSerializer(fr_user[0])
        # serialized_username.data["username"] é uma string com o Username do Usuário que realizou a FriendRequest
        # fr["id"] é o ID da FriendRequest
        response_fr = {"friend_request_id": fr["id"], "friend_request_user": serialized_username.data["username"]}
        lista_frs.append(response_fr)

    # Serializa o Usuário para retornar um dicionário com uma lista de amigos deste usuário
    # Retorna como response a lista de amigos
    this_user_friends_serialized = UserFriendsSerializer(this_user)
    this_user_friends_id_list = this_user_friends_serialized.data["friends"]
    this_user_friends_list = []
    for friend_id in this_user_friends_id_list:
        friend_user = all_users.filter(id=friend_id)
        friend_serialized_username = UsernameSerializer(friend_user[0]).data
        this_user_friends_list.append(friend_serialized_username["username"])

    response_data = {"friend_requests": lista_frs, "friends": this_user_friends_list}

    return Response(response_data)