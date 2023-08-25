from django import forms
from .models import NeonLights


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = NeonLights
        fields = ('image', 'name', 'description','meters', 'inches', 'ip_rating',)    
        widgets = {
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'meters': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'inches': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ip_rating': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = NeonLights
        fields = ('image', 'name', 'description','meters', 'inches', 'ip_rating',)    
        widgets = {
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'meters': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'inches': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ip_rating': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }