from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Apartment
from rest_framework.viewsets import ModelViewSet
from .serializers import ApartmentSerializer

class ApartmentsViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

def index(request):
    apartments= Apartment.objects.all()
    return JsonResponse(apartments, safe=False)