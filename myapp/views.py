from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from myapp.controllers.controller import Controller
# Create your views here.
from django.contrib.auth.decorators import login_required
import uuid
import json

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
    )\

@login_required
def distribucion(request):
    registros = Controller.get_registros_mesas()
    context = {'registros': registros}
    return render(
        request,
        'distribucion.html',
        context
    )

@login_required
def testigos(request):
    parameter_value = request.GET.get('with_null') in ['false', 'False']
    registros = Controller.get_resumen_registros(not parameter_value)
    context = {'registros': registros}
    return render(
        request,
        'resumen.html',
        context
    )


@login_required
def estadisticas(request):
    registros = Controller.get_resumen_registros_para_graficos()
    context = {'registros': registros}
    return render(
        request,
        'estadistica_v3.html',
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


@require_http_methods(["PUT"])
@csrf_exempt
def update_registro(request, uuid_param):
    data = json.loads(request.body.decode('utf-8'))
    # Busca el registro que coincide con el UUID y actualízalo

    response = Controller.actualiza_registro(uuid_param, data)

    return JsonResponse({"response": response})

