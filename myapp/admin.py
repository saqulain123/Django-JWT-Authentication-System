from django.contrib import admin
from .models import UserData
# Register your models here.
@admin.register(UserData)
class ModelUserData(admin.ModelAdmin):
    list_display=['name','email','date_joined']