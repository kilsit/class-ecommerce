from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Customer, Order, Product
# from .models import User, Order, Product
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address", "mobile", "email", "payment_method"]
        widgets = {
            "ordered_by": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
             "shipping_address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ur address here..."
            }),
            "mobile": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ur phone  here..."
  
           }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email  here..."
             }),
            "payment_method": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),

    }


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
     
    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]
      
    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists.")
        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    

class ProductForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))
    class Meta:
        model = Product
        fields = ["title", "slug", "category", "image", "marked_price", "selling_price", "description", "warranty", "return_policy"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
  
            }),

            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "category": forms.Select(attrs={
            "class": "form-control"
            }),
            "image": forms.ClearableFileInput(attrs={
            "class": "form-control"
            }),
            "marked_price": forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "marked price of the product"
            }),
            "selling_price": forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "selling price of the product"
            }),
            "description": forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Descriptions of the product...",
            "rows": 5,
            }),
            "warranty": forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the product warranty here...",
           
            }),
            "return_policy": forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the product return policy here...",
           
            }),
         

        }



class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with account does not exists...")
            
        return e

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Enter New Password',

    }), label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Confirm New Password',

    }),label="Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "new password did not match! ")
        return confirm_new_password

