from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        })
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email Address'
        })
