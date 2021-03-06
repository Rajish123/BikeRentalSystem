# path('profile_detail/<uuid:id>/')

from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import (
    RegisterView,LogutView,ChangePasswordView
)

urlpatterns = [
    path('register/',RegisterView.as_view(), name = 'register'),
    path('login/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('login/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('logout/',LogutView.as_view(),name = 'logout'),
    path('change_password/',ChangePasswordView.as_view(),name = 'change-password'),
]
