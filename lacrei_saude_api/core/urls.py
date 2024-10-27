from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterView, UserLoginView, UserDetailView, ProfissionalList, ProfissionalDetail

urlpatterns = [
    path('auth/register/', UserRegisterView.as_view(), name='user-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('profissionais/', ProfissionalList.as_view(), name='profissional-list'),
    path('profissionais/<int:id>/', ProfissionalDetail.as_view(), name='profissional-detail'),
]
