from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import *
from .serializers import *
# Create your views here.

class GameList(APIView):

    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)