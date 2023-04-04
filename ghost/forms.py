from django import forms


class dbDetails(forms.Form):
    database_name = forms.CharField(max_length=50)
    database_user = forms.CharField(max_length=20)
    database_password = forms.CharField(widget=forms.PasswordInput)
