from django import forms 
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("username is taken")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("a user with this email exists")
        return email