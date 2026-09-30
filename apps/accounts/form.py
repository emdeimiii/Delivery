from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """Форма регистрации с Bootstrap-классами."""
    email = forms.EmailField(
    required=True,
    label='Email',
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # Добавляем Bootstrap-класс всем полям
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})