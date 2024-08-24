from rest_framework import routers
from django.urls import path, include
from .views import AutorViewSet, LivroViewSet

router = routers.DefaultRouter()
router.register(r'autor', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]