from django import forms

class ColorSelectionForm(forms.Form):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
    ]

    player_color = forms.ChoiceField(
        label='Select Your Color',
        choices=COLOR_CHOICES,
        widget=forms.RadioSelect,
    )
