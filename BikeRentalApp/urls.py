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
    DetailRentedVehicle,
    CancelBooking,
    ReturnVehicleView,
    AvailableVehicles,
    GenerateBill,
    Payment
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
    # checked
    path('all_vehicles/<str:pk>/',AvailableVehicles.as_view(),name = 'all-vehicles'),
    
    #checked
    path('vehicle/<str:id>/',CreateReadVehicleView.as_view(),name = 'vehicle'),
    #checked
    # requires vehicle id
    path('update_vehicle/<str:pk>/',UpdatedDetailVehicleView.as_view(),name = 'update-vehicle'),
    # requries vechile id
    # checked
    path('rent_vehicle/<str:pk>/',RentVehicleView.as_view(), name = 'rent-bike'),
    # required rented_vehicle id
    # checked
    path('rented_vehicle_detail/<str:pk>/',DetailRentedVehicle.as_view(),name = 'updatedetail-rentedvehicle'),
    # path('return_vehicle/<str:pk>/',ReturnVehicleView.as_view(),name = 'return-vehicle')
    # checked
    # requires rentvehicle id
    path('cancel_booking/<str:pk>/',CancelBooking.as_view(),name = 'cancel-booking'),
    # requires rentvehicle id
    # checked
    path('return_vehicle/<str:pk>/',ReturnVehicleView.as_view(),name = 'return-vehicle'),
    # require rentvehicle id
    path('bill/<str:pk>/', GenerateBill.as_view(),name = 'bill'),
    # require bill id
    path('payment/<str:pk>/',Payment.as_view(),name = 'payment')

]
