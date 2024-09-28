from django.db import models
from django import forms

# Create your models here.
class Userdata(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.email
    
class Doctordetail(models.Model):
    doc_img=models.ImageField(upload_to='doctor/')
    doc_name=models.CharField(max_length=50)
    doc_spec=models.CharField(max_length=50)
    def __str__(self):
        return self.doc_name
    
class appointmentdetail(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    reason = models.CharField(max_length=255)
    number= models.IntegerField()
    doctor = models.ForeignKey(Doctordetail, on_delete=models.CASCADE)  # ForeignKey to Doctordetail

    def __str__(self):
        return f"Appointment for {self.name} with Dr. {self.doctor.doc_name}"

class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointmentdetail
        fields = ['number'] 

# forms.py


class adminloginform(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    ailment = models.TextField()
    doctor = models.ForeignKey(Doctordetail, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.patient_name

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.patient.patient_name}"
