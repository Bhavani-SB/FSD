from django.shortcuts import render, redirect
from .models import Userdata, Doctordetail, appointmentdetail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import adminloginform

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        user = Userdata.objects.filter(email=email)
        if user.exists():
            messages.error(request, "Email already taken")
        elif password != password2:
            messages.error(request, "Passwords do not match")
        else:
            Userdata.objects.create(email=email, password=password)
            return render(request, 'login.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Userdata.objects.filter(email=email, password=password)
        if user.exists():
            return redirect('/main/')
        else:
            messages.error(request, "Check your email and password")
    return render(request, 'login.html')

def main(request):
    doctors = Doctordetail.objects.all()
    return render(request, 'main.html', {'doctors': doctors})

def mainn(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")
        name = request.POST.get("name")
        age = request.POST.get("age")
        reason = request.POST.get("reason")
        number = request.POST.get("number")
        email = request.POST.get('email')

        try:
            doctor = Doctordetail.objects.get(doc_name=doctor_name)
        except Doctordetail.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('/mainn/')

        appointment = appointmentdetail.objects.filter(
            name=name, age=age, reason=reason, number=number, doctor=doctor, email=email
        )
        if appointment.exists():
            messages.error(request, "This appointment already exists.")
        else:
            appointmentdetail.objects.create(
                name=name,
                age=age,
                reason=reason,
                number=number,
                email=email,
                doctor=doctor
            )
            messages.success(request, "Appointment successfully booked!")
            return redirect('index')

    doctor_name = request.GET.get("doctor_name")  # Retrieve doctor name from query parameters
    return render(request, 'mainn.html', {'doctor_name': doctor_name})  # Pass doctor name to template

@login_required
def admin_view(request):
    appointments = appointmentdetail.objects.all()
    return render(request, 'admin.html', {'appointments': appointments})

ADMIN_PASSWORD = '130304@Bhava'  # Change this to your desired password

def admin_login(request):
    if request.method == 'POST':
        form = adminloginform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == ADMIN_PASSWORD:
                return redirect('admin_page')
            else:
                form.add_error('password', 'Incorrect password')
    else:
        form = adminloginform()
    return render(request, 'admin_login.html', {'form': form})

def admin_page(request):
    return render(request, 'admin_page.html')

def about(request):
    return render(request, 'about.html')
