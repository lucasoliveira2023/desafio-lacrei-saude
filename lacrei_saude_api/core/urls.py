from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProfissionalViewSet, ConsultaViewSet

router = DefaultRouter()
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'consulta', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
