from django import forms
from .models import Room, Doctordetail, Patient

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'is_available']



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name', 'age', 'ailment', 'doctor', 'room']
