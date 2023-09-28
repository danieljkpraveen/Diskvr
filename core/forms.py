from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    # phone_number = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2',)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user

    username = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'placeholder': 'Enter your Username',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'placeholder': 'Enter phone number',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs= {
                'placeholder': 'Provide your Email ID',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                'placeholder': 'Enter unique password',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                'placeholder': 'Repeat password for confirmation',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'placeholder': 'Enter your Username',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                'placeholder': 'Enter your password',
                'class': 'w-full py-4 px-6 rounded-xl text-black',
            }
        )
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Provide your Email ID',
                'class': 'w-full py-4 px-6 rounded-xl',
            }
        )
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter new password',
                'class': 'w-full py-4 px-6 text-black rounded-xl',
            }
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm new password',
                'class': 'w-full py-4 px-6 text-black rounded-xl',
            }
        )
    )