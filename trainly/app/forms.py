from django import forms
from allauth.socialaccount.forms import SignupForm
from . import models
from django.contrib.admin.widgets import AdminDateWidget


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='username')
    name = forms.CharField(max_length=30, label='name')

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.save()


class SearchTrainForm(forms.Form):
    from_station=forms.ModelChoiceField(queryset=models.TrainStops.objects.values_list('stop',flat=True).distinct(),widget=forms.Select(attrs={'class': 'form-control'}),empty_label="Select Station",to_field_name="stop")
    to_station=forms.ModelChoiceField(queryset=models.TrainStops.objects.values_list('stop',flat=True).distinct(),widget=forms.Select(attrs={'class': 'form-control'}),empty_label="Select Station",to_field_name="stop")
    date=forms.DateField(widget = forms.SelectDateWidget())
    seats=forms.IntegerField(min_value=1)
    class_type=forms.ModelChoiceField(queryset=models.TrainSeats.objects.values_list('class_type',flat=True).distinct(),widget=forms.Select(attrs={'class': 'form-control'}),empty_label="Select Station",to_field_name="class_type")
