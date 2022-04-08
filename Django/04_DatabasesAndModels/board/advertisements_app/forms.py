from django import forms
from advertisements_app.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta():
        model = Advertisement
        fields = '__all__'
