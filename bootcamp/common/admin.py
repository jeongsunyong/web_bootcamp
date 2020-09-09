from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm, CustomUserChangeForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form= CustomUserChangeForm
    model = CustomUser
    list_display=('username','email','phone','intro')
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)