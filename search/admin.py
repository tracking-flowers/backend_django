from django.contrib import admin
from django import forms
from .models import Category, Food
# Register your models here.

admin.site.register(Category)
admin.site.register(Food)