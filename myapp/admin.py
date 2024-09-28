from django.contrib import admin
from .models import Userdata,Doctordetail,appointmentdetail
# Register your models here.
admin.site.register(Userdata)
admin.site.register(Doctordetail)
admin.site.register(appointmentdetail)