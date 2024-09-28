from django.shortcuts import render,redirect
from .models import Userdata,Doctordetail,appointmentdetail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import adminloginform
from django.shortcuts import render, redirect
from .models import Room, Patient, Bill
from .forms import RoomForm, PatientForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        user=Userdata.objects.filter(email=email)
        if user.exists():
            messages.error(request,"Email already taken")
        elif password != password2:
            messages.error(request,"Password not match")
        else:
            Userdata.objects.create(email=email,password=password)
            return render(request,'login.html')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=Userdata.objects.filter(email=email,password=password)
        if user.exists():
            return redirect('/main/')
        else:
            messages.error(request,"Check email and password")
            
    return render(request,'login.html')

def main(request):
    doctor=Doctordetail.objects.all()
    return render(request,'main.html',{'doctors':doctor})

def mainn(request):
    if request.method == "POST":
        # Capture the data from the form
        doctor_name = request.POST.get("doctor_name")  # Ensure your form includes doctor_name
        name = request.POST.get("name")
        age = request.POST.get("age")
        reason = request.POST.get("reason")
        number =request.POST.get("number")
        
        try:
            # Fetch the doctor object based on the doctor name
            doctor = Doctordetail.objects.get(doc_name=doctor_name)  # Update this line
        except Doctordetail.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('/mainn/')  # Redirect if doctor not found

        # Check if the appointment already exists (optional validation)
        appointment = appointmentdetail.objects.filter(name=name, age=age, reason=reason,number=number, doctor=doctor)
        if appointment.exists():
            messages.error(request, "This appointment already exists.")
        else:
            # Create and save the appointment
            appointmentdetail.objects.create(
                name=name,
                age=age,
                reason=reason,
                number=number,
                doctor=doctor  # Save doctor reference in the appointment
            )
            messages.success(request, "Appointment successfully booked!")
            
            return redirect('index')  # Redirect after success
        
        
            
    # Always render the template with the list of doctors
    doctors = Doctordetail.objects.all()  # Fetch all doctors to display
    return render(request, 'mainn.html', {'doctors': doctors})  # Pass doctors to the template

@login_required
def admin_view(request):
    appointments = appointmentdetail.objects.all()  # Fetch all appointments
    return render(request, 'admin.html', {'appointments': appointments})





ADMIN_PASSWORD = '130304@Bhava'  # Change this to your desired password

def admin_login(request):
    if request.method == 'POST':
        form = adminloginform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == ADMIN_PASSWORD:
                return redirect('admin_page')  # Redirect to your admin page
            else:
                form.add_error('password', 'Incorrect password')
    else:
        form = adminloginform()
    
    return render(request, 'admin_login.html', {'form': form})

def admin_page(request):
    return render(request, 'admin_page.html')  # Your admin data template



# View to add a room
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Assuming you have a room listing view
    else:
        form = RoomForm()
    return render(request, 'hospital/add_room.html', {'form': form})



# View to add a patient
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Assuming you have a patient listing view
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})

# View to see reports
def view_reports(request):
    patients = Patient.objects.all()
    bills = Bill.objects.all()
    return render(request, 'view_reports.html', {'patients': patients, 'bills': bills})

def about(request):
    return render(request, 'about.html')

