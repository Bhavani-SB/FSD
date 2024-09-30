from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password  # Import for password hashing
from .models import Userdata, Doctordetail, appointmentdetail
from .models import adminloginform
from django.contrib.auth.decorators import login_required

# Home page view
def index(request):
    return render(request, 'index.html')

# Signup view
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if Userdata.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
        elif password != password2:
            messages.error(request, "Passwords do not match")
        else:
            Userdata.objects.create(email=email, password=password)
            return redirect('login')  
    return render(request, 'signup.html')
# Login view
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Userdata.objects.get(email=email)
            if check_password(password, user.password):  # Verify password using Django's built-in check
                request.session['user_id'] = user.id  # Store user ID in session
                return redirect('main')
            else:
                messages.error(request, "Incorrect password")
        except Userdata.DoesNotExist:
            messages.error(request, "User not found")
    return render(request, 'login.html')

# Main view to show doctors
def main(request):
    doctors = Doctordetail.objects.all()
    return render(request, 'main.html', {'doctors': doctors})

# Appointment booking view
def mainn(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")
        try:
            doctor = Doctordetail.objects.get(doc_name=doctor_name)
            # Proceed to create the appointment
        except Doctordetail.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('mainn')  # or whatever your redirect is


# Admin view (requires login)
@login_required
def admin_view(request):
    appointments = appointmentdetail.objects.all()
    return render(request, 'admin.html', {'appointments': appointments})

# Admin login with predefined password
ADMIN_PASSWORD = '130304@Bhava'

def admin_login(request):
    if request.method == 'POST':
        form = adminloginform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == ADMIN_PASSWORD:
                request.session['is_admin'] = True  # Store admin session data
                return redirect('admin_page')
            else:
                form.add_error('password', 'Incorrect password')
    else:
        form = adminloginform()
    return render(request, 'admin_login.html', {'form': form})

# Admin page (requires admin login)
def admin_page(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')  # Redirect if not logged in as admin
    return render(request, 'admin_page.html')

# About page
def about(request):
    return render(request, 'about.html')
