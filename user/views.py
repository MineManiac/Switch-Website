from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User
from .serializers import UserSerializer

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['GET', 'POST'])
def api_user(request, note_id):
    try:
        user = User.objects.get(id=note_id)
    except User.DoesNotExist:
        raise Http404()
    serialized_note = UserSerializer(user)
    return Response(serialized_note.data)