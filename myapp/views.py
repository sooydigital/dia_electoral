from django.shortcuts import render
from django.http import JsonResponse
from myapp.controllers.controller import Controller
# Create your views here.
from django.contrib.auth.decorators import login_required


def get_structure(request):
    user = request.user
    barrios = Controller.get_structure(user)

    response = {
        "data": barrios
    }
    return JsonResponse(response)

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    context = Controller.get_structure(user)
    mesa_list = [1, 2, 3]
    context = {'mesa_list': mesa_list}
    return render(
        request,
        'dashboard.html',
        context
    )

@login_required
def mesa(request, id):
    user = request.user
    context = Controller.get_structure(user)
    mesa_list = [1, 2, 3]
    context = {'mesa_list': mesa_list}
    return render(
        request,
        'mesa.html',
        context
    )