from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from core.views import ProfissionalViewSet, ConsultaViewSet
from core.views import ProfissionalList, ProfissionalDetail, UserRegisterView, UserLoginView, UserDetailView

urlpatterns = [
    path('profissionais/', ProfissionalList.as_view(), name='profissional-list'),
    path('profissionais/<int:id>/', ProfissionalDetail.as_view(), name='profissional-detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'), ##mantem a url para o detalhe do usuario
]
