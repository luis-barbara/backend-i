from django import forms
from characters.models import Character  

class CharacterForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Character
        fields = '__all__'

