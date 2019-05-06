from django import forms
from django.contrib.auth.models import User
from myapp.models import Looser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class LooserForm(forms.ModelForm):
    age = forms.IntegerField(widget=forms.NumberInput())

    class Meta():
        model = Looser
        fields = ('age',)
