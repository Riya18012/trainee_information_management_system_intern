from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Course, Trainee, Trainer, TrainingCenter, Enrollment, Certificate 
from .forms import CourseForm, TraineeForm, TrainerForm, TrainingCenterForm, EnrollmentForm, CertificateForm
from .decorators import user_is_admin
# Create your views here.

def Home(request):
    return render(request, 'trainee/home.html')

def About(request):
    return render(request, 'trainee/about.html')

def Contact(request):
    return render(request, 'trainee/contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    num_trainees = Trainee.objects.count()
    num_trainers = Trainer.objects.count()
    num_courses = Course.objects.count()
    num_training_centers = TrainingCenter.objects.count()
    num_certificates = Certificate.objects.count()
    num_enrollments = Enrollment.objects.count()

    context = {
        'num_trainees': num_trainees,
        'num_trainers': num_trainers,
        'num_courses': num_courses,
        'num_training_centers': num_training_centers,
        'num_certificates': num_certificates,
        'num_enrollments': num_enrollments,
    }
    
    return render(request, 'trainee/index.html', context)

def Login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error= "yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'trainee/login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('admin_login')

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def training_center_list(request):
    centers = TrainingCenter.objects.all()
    return render(request, 'trainee/training_center_list.html', {'centers': centers})

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'trainee/enrollment_list.html', {'enrollments': enrollments})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainee/trainer_list.html', {'trainers': trainers})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'trainee/course_list.html', {'courses': courses})

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'trainee/certificate_list.html', {'certificates': certificates})


@user_is_admin  # Apply the decorator
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to the list view
    else:
        form = CourseForm()
    return render(request, 'trainee/add_course.html', {'form': form})


@user_is_admin  # Apply the decorator
def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add_trainee.html', {'form': form})


@user_is_admin  # Apply the decorator
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')  # Redirect to the list view
    else:
        form = TrainerForm()
    return render(request, 'trainee/add_trainer.html', {'form': form})


@user_is_admin  # Apply the decorator
def add_training_center(request):
    if request.method == 'POST':
        form = TrainingCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_center_list')
    else:
        form = TrainingCenterForm()
    return render(request, 'trainee/add_training_center.html', {'form': form})


@user_is_admin  # Apply the decorator
def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'trainee/add_enrollment.html', {'form': form})


@user_is_admin  # Apply the decorator
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'trainee/add_certificate.html', {'form': form})