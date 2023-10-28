from django.urls import path
from django.views.generic import TemplateView
from myapp import views
# from rest_framework.authtoken.views import obtain_auth_token

app_name = "app"
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # path('api/token/', obtain_auth_token, name='api_token'),
    # path('api/items/', views.ItemList.as_view(), name='item-list'),
    # path('api/items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),

    path('api/get_structure', views.get_structure, name='get_structure'),
    # Otras URL de tu proyecto Django aquí
]