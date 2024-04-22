from django.contrib.auth.forms import PasswordChangeForm
from django.db import models
from django.forms import ModelForm
from users.models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Enter New Password Confirmation'
