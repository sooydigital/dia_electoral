from django.urls import path
from myapp import views

app_name = "app"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mesa/<str:id>', views.mesa, name='mesa'),
    path('update_registro/<uuid:uuid_param>/', views.update_registro, name='update_registro'),
    path('estadistica_por_encuestador', views.dashboard, name='estadistica_por_encuestador'),
    path('distribucion', views.distribucion, name='distribucion'),
    path('testigos', views.testigos, name='testigos'),
    path('estadisticas', views.distribucion, name='estadisticas'),
    path('geomapa', views.distribucion, name='geomapa'),
]
