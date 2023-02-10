from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Form, Port, Vessel, Passenger


class ParkingChangeForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['vessel', 'port', 'purpose', 'scheduled_departure', 'scheduled_arrival', 'form_filling_date']
        
class VesselChangeForm(forms.Form):
    model = Vessel
    fields = [
        'ctno', 'shipname', 'owner', 'contact_no', 'address', 
        'ship_kind', 'tonnage', 'length', 'width', 'max_capacity',
        'updated_at'
    ]

class PassengerChangeForm(forms.Form):
    model = Passenger
    fields = [
        'name', 'jobtitle', 'id_num', 'contact_no', 'emergency_contact_person',
        'emergency_contact_no', 'form'
    ]