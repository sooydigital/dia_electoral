from django.shortcuts import render
from django.http import JsonResponse
from myapp.controllers.controller import Controller
# Create your views here.

def get_structure(request):
    user = request.user
    barrios = Controller.get_structure(user)

    response = {
        "data": barrios
    }
    return JsonResponse(response)