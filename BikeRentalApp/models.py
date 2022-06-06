from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid as uuid_lib

# # Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid_lib.uuid4, unique=True, primary_key=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = PhoneNumberField()
    address = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to = 'profile_picture', default = 'default.jpg')

    def __str__(self):
        return self.user.username

#     # When a new instance is made for a model, django must know where to go when a new post is created or a new instance is created.
#     # Here get_absolute_url comes in picture. It tells the django where to go when new post is created.
    def get_absolute_url(self):
        return reverse("profile/", kwargs={"id": self.id})
        
# # we define signals so our Profile model will be automatically created/updated when we create/update User instances.
@receiver(post_save,sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

class Category(models.Model):
    TYPE = (
        ('bike','bike'),
        ('scooty','scooty')
    )
    type = models.CharField(max_length=25,choices=TYPE)
    image = models.ImageField(upload_to = 'category', default = 'default.jpg')

    def __str__(self):
        return f"{self.type}"

class Vehicle(models.Model):
    status = (
        ('available','available'),
        ('not-available','not-available')
    )
    # site = models.ForeignKey(Site, to_field='id', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='vehicles')
    company = models.CharField(max_length = 25)
    model_name = models.CharField(max_length=25)
    colour =models.CharField(max_length=25)
    booked = models.BooleanField(default=False)
    number_plate = models.IntegerField()
    review = models.TextField(max_length=250,null=True,blank=True)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'vehicle',default = 'default.jpg')
    vehicle_status = models.CharField(max_length=25, choices=status)


    def __str__(self):
        return f"{self.company}-->{self.model_name}"  

class RentVehicle(models.Model):
    rental_type = (
        ('Hourly','Hourly'),
        ('Daily','Daily'),
        ('Weekly','Weekly'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uservehicle')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    renttype = models.CharField(max_length = 25,choices=rental_type)
    duration = models.IntegerField()
    license_number = models.BigIntegerField()
    license = models.FileField(upload_to='document/')
    rented_at = models.DateTimeField(auto_now_add = True)
    returned_at = models.DateTimeField(auto_now = True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.vehicle.model_name}"


# new
# class Bill(models.Model):
#     rented_vehicle = models.ForeignKey(RentVehicle,on_delete = models.CASCADE)
#     returned_at = models.DateTimeField(auto_now_add = True)
#     total_bill = models.FloatField()

#     def save(self,*args,**kwargs):
#         rented_date = self.rented_vehicle.rented_at
#         if self.rented_vehicle.rental_type == 'Hourly':
#             total_bill = 100
#         elif self.rented_vehicle.rental_type == 'Daily':
#             total_bill = 200
#         elif self.rented_vehicle.rental_type == 'Weekly':
#             total_bill = 300
            
#         super(Bill,self).save(*args,**kwargs)
    
#     def __str__(self):
#         return f"{self.rented_vehicle.user.username}-->{self.total_bill}"











