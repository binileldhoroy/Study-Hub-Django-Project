from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)