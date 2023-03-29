from django import forms

class dbDetails(forms.Form):
    dbName = forms.CharField(max_length=50)
    dbUser = forms.CharField(max_length=20)
    dbPassword = forms.CharField(widget=forms.PasswordInput)
