from django.contrib import admin

from .models import Profile, Reservation, Room, Category

admin.site.register(Profile)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Category)