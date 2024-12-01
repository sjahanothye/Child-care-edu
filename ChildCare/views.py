from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from .models import Parents
from .models import Child
from .models import Doctor
from .models import Consultation
from .models import HealthInfo
from .models import LearningPlan
from .models import Schedule
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages

from django.shortcuts import render, get_object_or_404




# Create your views here.
def Home(request):
    return render(request, template_name='ChildCare\home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, message="Login successful!")
            return redirect('home')  # Redirect to home page or any other page after login
        else:
            messages.error(request, message="Invalid username or password!")
            return redirect('login')  # Redirect to login page if authentication fails

    return render(request, template_name='ChildCare/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, message="You have been logged out.")
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, message="Passwords do not match!")
            return redirect('signup')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, message="Username already exists!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, message="Email already registered!")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log the user in
        login(request, user)
        messages.success(request, message="Signup successful!")
        return redirect('home')

    return render(request, template_name='ChildCare/signup.html')

def parents(request):
    # Fetching the data from the Parent model
    object_project = Parents.objects.all()  # Retrieve all Parent objects

    # Passing the data to the template
    return render(request, template_name='ChildCare/Parents.html',context= {'object_project': object_project})


def child(request):
    object_child = Child.objects.all()  # Fetch all child records
    return render(request, template_name='Child.html',context= {'object_child': object_child})

def view_certificate(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    return render(request, template_name='ChildCare/view_certificate.html',contex= {'child': child})


def consultation(request):
    consultations = Consultation.objects.all()  # Fetch all consultation records
    context = {
        'object_project': consultations,  # Match the key with the template
    }
    return render(request, template_name='ChildCare/Consultation.html', context=context)


def healthInfo(request):
    healthinfo = HealthInfo.objects.all()  # Fetch all HealthInfo records
    context = {
        'object_project': healthinfo,  # Match the key with the template
    }
    return render(request, template_name='ChildCare/HealthInfo.html', context=context)



def schedule(request):
    schedule_data = Schedule.objects.all()  # Fetch all records
    context = {
        'object_project': schedule_data,  # Match the template variable
    }
    return render(request, template_name='ChildCare/Schedule.html', context=context)


def learningPlan(request):
    learningplan = LearningPlan.objects.all()  # Fetch all LearningPlan records
    context = {
        'object_project': learningplan,  # Match the key with the template
    }
    return render(request, template_name='ChildCare/LearningPlan.html', context=context)


def doctor(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    context = {
        'object_project': doctors,  # Use 'object_project' as the context key
    }
    return render(request, template_name='ChildCare/Doctor.html', context=context)



