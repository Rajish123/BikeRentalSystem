from django.urls import path

from .views import (
    UpdateProfile,
    ViewProfile,
)

urlpatterns = [
    path('view_profile/', ViewProfile.as_view(),name = 'view-profile'),
    path('update_profile/', UpdateProfile.as_view(),name = 'update-profile'),
]
