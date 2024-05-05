# forms.py
from django import forms
from .models import Club, Sport

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'location', 'sport', 'image']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='Club Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter club name',
                'class': 'form-control',
                'id': 'name'
            }
        )
    )

    location = forms.CharField(
        max_length=100,
        required=True,
        label='Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter location',
                'class': 'form-control',
                'id': 'location'
            }
        )
    )

    sport = forms.ModelChoiceField(
        queryset=Sport.objects.all(),
        required=True,
        label='Sport',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'sport'
            }
        )
    )

    image = forms.ImageField(
        required=False,
        label='Image',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        )
    )
