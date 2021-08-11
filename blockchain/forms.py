from django import forms
from .models import Block

class BlockForm(forms.ModelForm):
    name = forms.CharField(label='От кого')
    amount = forms.IntegerField(label='Сумма')
    to_whom = forms.CharField(label='Кому')

    class Meta:
        model = Block
        exclude = {'prev_hash'}
