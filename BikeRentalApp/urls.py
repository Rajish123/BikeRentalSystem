from django.urls import path

from .views import (
    DashBoard,
    ReturnVehicleView,
    UpdateProfile,
    ViewProfile,
    CreateCategoryView,
    ReadCategoryView,
    UpdateCategoryView,
    CreateVehicleView,
    UpdatedVehicleView,
    DetailVehicleView,
    RentVehicleView,
    DetailRentedVehicle,
    CancelBooking,
    ReturnVehicleView,
    AvailableVehicles,
    GenerateBill,
    Payment,
    DashBoard
)

urlpatterns = [
    #checked
    path('view_profile/', ViewProfile.as_view(),name = 'view-profile'),
    #checked
    path('update_profile/', UpdateProfile.as_view(),name = 'update-profile'),
    #checked
    path('create_category/',CreateCategoryView.as_view(),name = 'category'),
    path('category/',ReadCategoryView.as_view(),name = 'category'),


    #checked
    path('update_category/<str:pk>/',UpdateCategoryView.as_view(),name = 'update-category'),
       #checked
    path('create_vehicle/<str:id>/',CreateVehicleView.as_view(),name = 'vehicle'),
    # in get method need vehicle id to get vehicles
    # need category id to add vehicles
    # checked
    path('vehicles/<str:pk>/',AvailableVehicles.as_view(),name = 'all-vehicles'),
    path('update_vehicle/<str:pk>/',UpdatedVehicleView.as_view(),name = 'update-vehicle'),

    #checked
    # requires vehicle id
    path('detail_vehicle/<str:pk>/',DetailVehicleView.as_view(),name = 'update-vehicle'),
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
    # save method not working but working from admin
    path('bill/<str:pk>/', GenerateBill.as_view(),name = 'bill'),
    # require bill id
    path('payment/<str:pk>/',Payment.as_view(),name = 'payment'),
    path('dashboard/',DashBoard.as_view(),name = 'dashboard')

]
