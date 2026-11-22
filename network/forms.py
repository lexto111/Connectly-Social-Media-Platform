from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location']

        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder': 'Write something about yourself...',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter your location'
            }),
        }