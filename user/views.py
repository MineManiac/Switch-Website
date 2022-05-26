from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User
from .serializers import UserSerializer



def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])
def api_note(request, note_id):

    try:
        user = User.objects.get(id=note_id)
    except User.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_note_data = request.data
        user.title = new_note_data['title']
        user.content = new_note_data['content']
        user.save()

    serialized_note = UserSerializer(user)
    return Response(serialized_note.data)
