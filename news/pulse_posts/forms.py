from django import forms


class PostsPulse(forms.Form):
    ticker = forms.CharField(label='ticker', max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Тикер бумаги'}))
    num_posts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Кол-во постов'}))
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)

class GraphForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Дата начала'}))
    ticker = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Тикер бумаги'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Дата конца'}))
    investor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Инвестор'}))
    is_holiday = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'check1', 'checked': '{true}'}))
