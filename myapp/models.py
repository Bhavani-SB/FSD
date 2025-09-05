from django.db import models
from django import forms

# Userdata model (assuming you're managing your own users)
class Userdata(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)  # Increase length for hashed passwords

    def __str__(self):
        return self.email

class Doctordetail(models.Model):
    doc_img = models.ImageField(upload_to='doctor/')
    doc_name = models.CharField(max_length=50)
    doc_spec = models.CharField(max_length=50)

    def __str__(self):
        return self.doc_name

class appointmentdetail(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    reason = models.CharField(max_length=255)
    number = models.CharField(max_length=100) 
    email = models.EmailField()
    doctor = models.ForeignKey(Doctordetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.name} with {self.doctor.doc_name}"

# Admin login form
class adminloginform(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
