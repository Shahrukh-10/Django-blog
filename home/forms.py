from django import forms
from .models import Contact
from django.forms.models import BaseModelForm


class ContactInfo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("Name", "PhoneNo", "Email", "Issue")
        widgets = {
            "Name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "name"}
            ),
            "PhoneNo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Phone No",
                    "type": "number",
                    "maxlength": 13,
                    "minlength": 10,
                }
            ),
            "Email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Email",
                    "type": "email",
                }
            ),
            "Issue": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tell us about your issue",
                }
            ),
        }
