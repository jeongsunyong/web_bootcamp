from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth import get_user_model

from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
class UserForm(UserCreationForm): #이메일 등 부가 속성을 주기 위해서는 UserCreationForm상속해서 만듬
    email = forms.EmailField(label="email")
    phone = forms.CharField(label="phone")
    intro = forms.CharField(widget=forms.Textarea )

    class Meta:
        model = CustomUser
        fields = ("username","email","phone","intro",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ("email","phone","intro",) #형식맞춰줘야함