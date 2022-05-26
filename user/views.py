from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User
from .serializers import UserSerializer
import requests

def novidade_games(request):
    url = "https://gaming-news.p.rapidapi.com/news"

    headers = {
	    "X-RapidAPI-Host": "gaming-news.p.rapidapi.com",
	    "X-RapidAPI-Key": "431b871e74msha3177211b2d7899p1645e3jsnde8a9570000a"
    }

    response = requests.request("GET", url, headers=headers)

    return response.text #Se quiser testar, coloque return HttpResponse(response.text)


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET'])
def api_news(request):

    data = novidade_games()

    

    # if request.method == 'GET':
    #     Nota = Note(Pais = data['country'], 
    #     NumCasos = data['cases']['total'], 
    #     NumNovosCasos = data['cases']['new'],
    #     NumMortes = data['deaths']['total'],
    #     NumNovasMortes = data['deaths']['new'])

    print(data)
