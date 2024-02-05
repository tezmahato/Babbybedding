from django import forms


class userform(forms.Form):
    username=forms.CharField(label="Username")
    email=forms.EmailField(label="Email")
    password=forms.CharField(label="Password")
    confirmPassword= forms.CharField(label="Password")
    
