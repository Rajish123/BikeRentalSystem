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
    company = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.type}-->{self.company}"

class Vehicle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=30)
    colour =models.CharField(max_length=30)
    booked = models.BooleanField(default=False)
    number_plate = models.IntegerField()
    review = models.TextField(max_length=250)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.model_name}-->{self.category.type}"  

class RentVehicle(models.Model):
    rental_type = (
        ('Hourly','Hourly'),
        ('Daily','Daily'),
        ('Weekly','Weekly'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    renttype = models.CharField(max_length = 25,choices=rental_type)
    duration = models.IntegerField()
    license_number = models.BigIntegerField()
    license = models.FileField(upload_to='document/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}-{self.vehicle.model_name}"



