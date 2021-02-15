from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Reservation(models.Model):
    check_in_date =  models.DateField()
    check_out_date = models.DateField()
    room_number = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Profile', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.check_out_date)

class Room(models.Model):
    room_number = models.IntegerField(unique = True)
    room_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    works = models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_number)

class Category(models.Model):
    name_of_category = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    cost_per_days = models.IntegerField()
    additional_Info = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='Category_photo')
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name_of_category

