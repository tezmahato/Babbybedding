from django import forms


class userform(forms.Form):
    Username=forms.CharField(label="Username")
    Email=forms.EmailField(label="Email")
    Password=forms.CharField(label="Password")
    ConfirmPassword= forms.CharField(label="Password")
    
