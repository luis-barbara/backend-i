from django import forms
from characters.models import Character  

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'gender', 'age', 'skin', 'ethnicity', 'eye_color', 'hair_color', 
            'hair_style', 'clothing', 'clothing_style', 'accessories', 'expression', 
            'pose', 'lighting', 'additional_details', 'image_type', 'style', 'texture', 
            'dominant_colors', 'contrast', 'shading'
        ]
