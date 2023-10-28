from django.urls import path
from myapp import views

app_name = "app"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('estadistica_por_encuestador', views.dashboard, name='estadistica_por_encuestador'),
]
