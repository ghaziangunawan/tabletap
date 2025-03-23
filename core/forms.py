from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class sign_up_form(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    terms = forms.BooleanField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data
    
    def save(self):
        full_name = self.cleaned_data["full_name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        name_split = full_name.split(" ",1)
        first_name = name_split[0]
        if len(name_split) > 1:
            last_name = name_split[1]
        else:
            last_name = name_split[0]
        try:
            user = User.objects.create_user(username=email, 
                                first_name=first_name, 
                                last_name=last_name, email=email, 
                                password=password)
        except:
            raise ValidationError("Something wrong with creating the data")
        user.save()
        return user


class login_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise ValidationError("Invalid login credentials")
            self.user = user
        return cleaned_data
    
    def get_user(self):
        return getattr(self, 'user', None)