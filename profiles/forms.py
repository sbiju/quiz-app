from django import forms

from .models import MasterProfile, ParticipantProfile


class MasterProfileForm(forms.ModelForm):
    class Meta:
        model = MasterProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'photo',
            'gender',
            'user',
            ]

        
class ParticipantProfileForm(forms.ModelForm):

    class Meta:
        model = ParticipantProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'photo',
            'gender',
            'created_by',
            ]