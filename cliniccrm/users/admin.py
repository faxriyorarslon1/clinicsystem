from django.contrib import admin
from .models import User, Doctor
# Register your models here.

admin.site.register(Doctor)
admin.site.register(User)
