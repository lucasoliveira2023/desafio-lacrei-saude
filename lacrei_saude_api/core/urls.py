from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from core.views import ProfissionalViewSet, ConsultaViewSet
from core.views import ProfissionalList, ProfissionalDetail

urlpatterns = [
    path('profissionais/', ProfissionalList.as_view(), name='profissional-list'),
    path('profissionais/<int:id>/', ProfissionalDetail.as_view(), name='profissional-detail'),
]
