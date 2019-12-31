from django import forms
from .models import Message


class AuthForm(forms.Form):
    name = forms.CharField(max_length=200, label="Your name")
    password = forms.CharField(max_length=323, widget=forms.PasswordInput, label="Gift Unlock Password")


class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, label="Name of your friend")
    text = forms.CharField(max_length=1000, widget=forms.Textarea({'placeholder': 'ex- Hello Name; Happy New Year; '
                                                                                  'How are you...'}), required=True,
                           label="Message separated by ';' "
                                 "separator")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True, label='Gift Unlock Password('
                                                                                               'Not your login '
                                                                                               'password)')
    image = forms.ImageField(required=False, label="Any background Image(optional)")

    class Meta:
        model = Message
        fields = [
            'name',
            'password',
            'text',
            'image',
        ]
