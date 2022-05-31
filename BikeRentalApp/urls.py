from django.urls import path

from .views import (
    UpdateProfile,
    ViewProfile,
    CreateReadCategoryView,
    UpdateCategoryView,
    CreateReadVehicleView,
    UpdatedDetailVehicleView
)

urlpatterns = [
    path('view_profile/', ViewProfile.as_view(),name = 'view-profile'),
    path('update_profile/', UpdateProfile.as_view(),name = 'update-profile'),
    path('category/',CreateReadCategoryView.as_view(),name = 'category'),
    path('update_category/<str:pk>/',UpdateCategoryView.as_view(),name = 'update-category'),

    # in get method need vehicle id to get vehicles
    # need category id to add vehicles
    path('vehicle/<str:id>/',CreateReadVehicleView.as_view(),name = 'vehicle'),
    path('update_vehicle/<str:pk>/',UpdatedDetailVehicleView.as_view(),name = 'update-vehicle')
]
