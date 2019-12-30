from django import forms
from .models import Message

class AuthForm(forms.Form):
    name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=323, widget=forms.PasswordInput)


class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True)
    text = forms.CharField(max_length=1000, widget=forms.Textarea(), required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = [
            'name',
            'password',
            'text',
            'image',
        ]
