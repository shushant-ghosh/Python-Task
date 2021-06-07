from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.DefaultRouter()
router.register(r'truck', views.TrucksViewSet)
router.register(r'permit', views.PermitViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),

]
