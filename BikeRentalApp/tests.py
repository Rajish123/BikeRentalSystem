from django.test import TestCase
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from BikeRentalProject.settings import BASE_DIR
from datetime import datetime
# get_user_model is reference to our active user
from django.contrib.auth import get_user_model

# Create your tests here.
class CategoryTest(TestCase):

    def setUp(self):
        image = SimpleUploadedFile(
            name='bike.jpeg', 
            content=open(os.path.join(BASE_DIR, 'media/category/bike.jpeg'), 'rb').read(), 
            content_type='image/jpeg')

        self.category = Category.objects.create(type='bike',image = image)

    def test_string_representation(self):
        category = Category(type = "bike")
        self.assertEqual(str(category),"bike")
        self.assertTrue(isinstance(category,Category))

    def test_category_content(self):
        self.assertEqual(f'{self.category.type}','bike')
        self.assertEqual(len(Category.objects.all()),1)

class VehicleTest(TestCase):
    def setUp(self):

        category_image = SimpleUploadedFile(
            name='bike.jpeg', 
            content=open(os.path.join(BASE_DIR, 'media/category/bike.jpeg'), 'rb').read(), 
            content_type='image/jpeg')
        vehicle_image = SimpleUploadedFile(
            name='duke200.webp', 
            content=open(os.path.join(BASE_DIR, 'media/vehicle/duke200.webp'), 'rb').read(), 
            content_type='image/webp')
        self.category = Category.objects.create(type='bike',image = category_image)
        self.vehicle = Vehicle.objects.create(
            category = self.category,
            company = "KTM",
            model_name = "Duke_200",
            colour = "orange",
            booked = False,
            number_plate = 1234,
            review = "Good",
            rate = 100,
            created_at = datetime.now(),
            updated_at = datetime.now(),
            image = vehicle_image,
            vehicle_status = "available"
        )

    def test_vehicle_string(self):
        vehicle = Vehicle(model_name = "Duke_200")
        self.assertEqual(f"{str(vehicle)}","-->Duke_200")
        self.assertTrue(isinstance(vehicle,Vehicle))

    def test_vehicle_count(self):
        self.assertEqual(len(Vehicle.objects.all()),1)

    def test_vehicle_content(self):
        self.assertEqual(f'{self.vehicle.category}',f'{self.category}')
        self.assertEqual(f'{self.vehicle.company}','KTM')
        self.assertEqual(f'{self.vehicle.model_name}','Duke_200')
        self.assertEqual(f'{self.vehicle.colour}','orange')
        self.assertEqual(f'{self.vehicle.booked}','False')
        self.assertEqual(f'{self.vehicle.number_plate}','1234')
        self.assertEqual(f'{self.vehicle.review}','Good')
        self.assertEqual(f'{self.vehicle.rate}','100')
        self.assertEqual(f'{self.vehicle.vehicle_status}','available')

# class RentVehicleTest(TestCase):
#     def setUp(self):
#         category_image = SimpleUploadedFile(
#             name='bike.jpeg', 
#             content=open(os.path.join(BASE_DIR, 'media/category/bike.jpeg'), 'rb').read(), 
#             content_type='image/jpeg')

#         vehicle_image = SimpleUploadedFile(
#             name='duke200.webp', 
#             content=open(os.path.join(BASE_DIR, 'media/vehicle/duke200.webp'), 'rb').read(), 
#             content_type='image/webp')

#         license = SimpleUploadedFile(
#             name='duke200.webp', 
#             content=open(os.path.join(BASE_DIR, 'media/document/coverletter.pdf'), 'rb').read(), 
#             content_type='file/pdf')



#         self.user = get_user_model().objects.create_user(
#             username = 'testuser',
#             email = 'test@user.com',
#             password = 'hidden'
#         )

#         self.category = Category.objects.create(type='bike',image = category_image)

#         self.vehicle = Vehicle.objects.create(
#             category = self.category,
#             company = "KTM",
#             model_name = "Duke_200",
#             colour = "orange",
#             booked = False,
#             number_plate = 1234,
#             review = "Good",
#             rate = 100,
#             created_at = datetime.now(),
#             updated_at = datetime.now(),
#             image = vehicle_image,
#             vehicle_status = "available"
#         )


#         self.rentvehicle = RentVehicle.objects.create(
#             user = self.user,
#             vehicle = self.vehicle,
#             renttype = 'Hourly',
#             duration = 10,
#             license_number = 1234,
#             license = license,
#             rented_at = datetime.now(),
#             returned_at = datetime.now(),
#             returned = False
#         )

#     def test_rentvehicle_string(self):
#         rentvehicle = RentVehicle()
#         self.assertEqual(f"{str(rentvehicle)}","-->Duke_200")
#         self.assertTrue(isinstance(rentvehicle,RentVehicle))



        



        

