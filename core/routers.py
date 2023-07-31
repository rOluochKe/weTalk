from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()

# Auth
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
# router.register(r"auth/login", LoginViewSet, basename="auth-login")
# router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
# router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")

# User
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]
