from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', 1234567890)
        firstname = request.POST.get('fname','')
        lastname = request.POST.get('lname','')
        password = request.POST.get('pass','')
        pdcheck = request.POST.get('pdcheck','false')
        try:
            user = User.object.get(email=email)
            return render(request, '')
        except User.DoesNotExist:
            user = User.objects.create(
                email=email, 
                first_name = firstname, 
                last_name = lastname,
                password = password,)
        if pdcheck == 'false':
            try:
                patient = Patient.objects.get(user_id = user)
                return render(request, '')
            except Patient.DoesNotExist:
                patient = Patient.objects.create(
                    user_id = user,
                    mobile_number = contact
                )
                return render(request, '')
        else:
            try:
                doctor = Doctor.objects.get(user_id = user)
                return render(request, '')
            except Doctor.DoesNotExist:
                dspec = request.POST.get('spec','')
                doctor = Doctor.objects.create(
                    user_id = user,
                    mobile_number = contact,
                    qualifiation = dspec
                )
                return render(request, '')

def login(request):
    if request.method == "POST":
        pdcheck = request.POST.get('pdcheck', 'false')
        email = request.POST.get('email','')
        password = request.POST.get('pass','')
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            ValueError('User Not found')
        if user.exists():
            user.password == password
        
        if pdcheck == 'false':
            try:
                patient = Patient.objects.get(user_id = user)
            except Patient.DoesNotExist:
                ValueError('Not a patient with this username')
        else:
            try:
                doctor = Doctor.objects.get(user_id = user)
            except Doctor.DoesNotExist:
                ValueError('Not a doctor with this username')
        
        return render(request, '')

@login_required
def book(request, doctor_id):
    try:
        patient = Patient.objects.get(
            user_id_id = request.user.id)
        doctor = Doctor.objects.get(
            user_id_id = doctor_id
        )
    except Patient.DoesNotExist or Doctor.DoesNotExist:
        raise ValueError('patient or doctor doesnt exist')
    
    appointment = Appointment.objects.create(
        patient_id = patient,
        doctor_id = doctor,
        date = request.POST.get('date', datetime.date.today() + 1),
        time = request.POST.get('time', datetime.time.now()),
        reason = request.POST.get('reason'),
        prior_reports = request.POST.get('prior_reports')
    )
    return render(request, '', {'appointment':appointment})

@login_required
def find_doctor(request):
    doctors = Doctor.objects.all()
    return render(request, '', {'doctors': doctors})

@login_required
def approve(request):
    try:
        doctor = Doctor.objects.get(
            user_id_id = request.user.id)
    except Doctor.DoesNotExist:
        raise ValueError("Doctor is not correct")
    appointments = Appointment.objects.filter(
        doctor_id = doctor,
        is_approved = None)
    return render(request, '', {'appointments': appointments})    

"""
    TEMPLATE JINJA CODE

    for doctor_appointment in doctor_appointments:
    if <select tick>:
        doctor_appointment.is_approved = True 
        doctor_appointment.save(update = True)
    else:
        doctor_appointment.is_approved = False
        doctor_appointment.save(update = True)
    """


    




            



            