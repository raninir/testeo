from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario, Mascota
from .serializers import MascotaSerializer
import json
# Create your views here.

class MascotaApiShow(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

  