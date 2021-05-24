from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_patient', 'is_doctor', 'is_superuser')


admin.site.register(User, UserAdmin)
