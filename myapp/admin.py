from django.contrib import admin
from .models import Userdata, Doctordetail, appointmentdetail  # Import your models

class AppointmentDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'doctor', 'email')  # Adjusted field names to match your model
    search_fields = ('doctor__doc_name', 'doctor__doc_spec', 'name', 'email')  # Updated fields for search

    def get_queryset(self, request):
        # Allow superusers to view all appointments
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        # Get the doctor instance associated with the current user
        try:
            doctor_instance = Doctordetail.objects.get(user=request.user)
            return qs.filter(doctor=doctor_instance)
        except Doctordetail.DoesNotExist:
            return qs.none()  # Return an empty queryset if the doctor instance does not exist

# Register all the models with the admin site
admin.site.register(Userdata)  # Manage Userdata in the admin panel
admin.site.register(Doctordetail)  # Manage Doctordetail in the admin panel
admin.site.register(appointmentdetail, AppointmentDetailAdmin)  # Manage appointmentdetail with custom admin
