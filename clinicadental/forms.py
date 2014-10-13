from django import forms
from clinicadental.models import MakeAppointment



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = MakeAppointment
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    phone_number = forms.IntegerField()
    cc_myself = forms.BooleanField(required=False)