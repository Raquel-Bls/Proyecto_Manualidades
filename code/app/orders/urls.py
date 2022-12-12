from django.urls import path
from .views import *
# Create your views here.

urlpatterns = [
    path('<int:pk>/', OrdersPageView.as_view(), name='orders'),
    path('charge/', charge, name='charge'),
    path('<int:pk>/', OrdersCurso.as_view(), name='pago_cursos')
]
