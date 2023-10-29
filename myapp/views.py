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

    mesas = Controller.get_mesas_by_user(user)
    context = {'mesa_list': mesas}
    return render(
        request,
        'dashboard.html',
        context
    )

@login_required
def mesa(request, id):
    user = request.user
    registros = Controller.get_distribucion_by_mesa_and_user(user, mesa_id=id)

    context = {'registros': registros}
    return render(
        request,
        'mesa.html',
        context
    )