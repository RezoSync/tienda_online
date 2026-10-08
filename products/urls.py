from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from .views import precio_final

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls

urlpatterns += [
	path('products/<int:pk>/precio-final/', precio_final),
]