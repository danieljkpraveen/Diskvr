from django import forms
from .models import NeonLights


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border bg-gray-800 text-white"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = NeonLights
        fields = (
            "image",
            "name",
            "price",
            "description",
            "inches",
            "ip_rating",
            "led_lights_used",
            "sheet_mm",
        )
        widgets = {
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "inches": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "ip_rating": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "led_lights_used": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "sheet_mm": forms.TextInput(attrs={"class": INPUT_CLASSES}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = NeonLights
        fields = (
            "image",
            "name",
            "price",
            "description",
            "inches",
            "ip_rating",
            "led_lights_used",
            "sheet_mm",
        )
        widgets = {
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "inches": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "ip_rating": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "led_lights_used": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "sheet_mm": forms.TextInput(attrs={"class": INPUT_CLASSES}),
        }
