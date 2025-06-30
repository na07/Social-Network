from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Подтверждение пароля"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
        }
        help_texts = {
            'username': '',  # убирает стандартное help_text
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Пароли не совпадают.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # хеширует пароль
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )
