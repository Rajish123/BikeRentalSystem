from django.urls import path

from .views import (
    ReturnVehicleView,
    UpdateProfile,
    ViewProfile,
    CreateReadCategoryView,
    UpdateCategoryView,
    CreateReadVehicleView,
    UpdatedDetailVehicleView,
    RentVehicleView,
    UpdateDetailRentedVehicle,
    CancelBooking,
    ReturnVehicleView,
    AvailableVehicles,
)

urlpatterns = [
    #checked
    path('view_profile/', ViewProfile.as_view(),name = 'view-profile'),
    #checked
    path('update_profile/', UpdateProfile.as_view(),name = 'update-profile'),
    #checked
    path('category/',CreateReadCategoryView.as_view(),name = 'category'),
    #checked
    path('update_category/<str:id>/',UpdateCategoryView.as_view(),name = 'update-category'),
    # in get method need vehicle id to get vehicles
    # need category id to add vehicles
    path('all_vehicles/<str:pk>/',AvailableVehicles.as_view(),name = 'all-vehicles'),
    
    #checked
    path('vehicle/<str:id>/',CreateReadVehicleView.as_view(),name = 'vehicle'),
    #checked
    path('update_vehicle/<str:pk>/',UpdatedDetailVehicleView.as_view(),name = 'update-vehicle'),
    # requries vechile id
    # checked
    path('rent_vehicle/<str:pk>/',RentVehicleView.as_view(), name = 'rent-bike'),
    # required rented_vehicle id
    path('update_rent_vehicle/<str:pk>/',UpdateDetailRentedVehicle.as_view(),name = 'updatedetail-rentedvehicle'),
    # path('return_vehicle/<str:pk>/',ReturnVehicleView.as_view(),name = 'return-vehicle')
    # checked
    # requires rentvehicle id
    path('cancel_booking/<str:pk>/',CancelBooking.as_view(),name = 'cancel-booking'),
    # requires rentvehicle id
    path('return_vehicle/<str:pk>/',ReturnVehicleView.as_view(),name = 'return-vehicle'),

]
