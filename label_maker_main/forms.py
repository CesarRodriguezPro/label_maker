from django import forms


class uploadForm(forms.Form):
    upload_file = forms.FileField()
