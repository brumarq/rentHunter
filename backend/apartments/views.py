from django.http.response import JsonResponse
from django.shortcuts import render

def index(request):
    apartments= []
    return JsonResponse(apartments, safe=False)