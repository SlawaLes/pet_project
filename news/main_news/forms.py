from django import forms

class ImageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 483px; height: 401px;'}))
