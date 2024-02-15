from django import forms


class PostsPulse(forms.Form):
    ticker = forms.CharField(label='ticker', max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Тикер бумаги'}))
    num_posts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Кол-во постов'}))
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
