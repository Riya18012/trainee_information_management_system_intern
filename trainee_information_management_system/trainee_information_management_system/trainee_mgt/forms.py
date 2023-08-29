from django import forms
from .models import Course, Trainee, Trainer, TrainingCenter, Enrollment, Certificate

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'trainer', 'training_center']
        labels = {
            'title': 'Course Title',
            'description': 'Description',
            'trainer': 'Trainer',
            'training_center': 'Training Center',
        }
        placeholders = {
            'title': 'Enter course title',
            'description': 'Enter course description',
            'trainer': 'Select a trainer',
            'training_center': 'Select a training center',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'address', 'course']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'date_of_birth': 'Date of Birth',
            'address': 'Address',
            'course': 'Course',
        }
        placeholders = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email',
            'phone_number': 'Enter your phone number',
            'date_of_birth': 'Select your date of birth',
            'address': 'Enter your address',
            'course': 'Select a course',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'specialization', 'designation']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'specialization': 'Specialization',
            'designation': 'Designation',
        }
        placeholders = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'email': 'Enter email',
            'phone_number': 'Enter phone number',
            'specialization': 'Enter specialization',
            'designation': 'Enter designation',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')

class TrainingCenterForm(forms.ModelForm):
    class Meta:
        model = TrainingCenter
        fields = ['name', 'location']
        labels = {
            'name': 'Training Center Name',
            'location': 'Location',
        }
        placeholders = {
            'name': 'Enter training center name',
            'location': 'Enter training center location',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['trainee', 'course', 'enrollment_date', 'training_period']
        labels = {
            'trainee': 'Trainee',
            'course': 'Course',
            'enrollment_date': 'Enrollment Date',
            'training_period': 'Training Period (in months)',
        }
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }
        placeholders = {
            'trainee': 'Select a trainee',
            'course': 'Select a course',
            'enrollment_date': 'Select enrollment date',
            'training_period': 'Enter training period',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['trainee', 'course', 'issue_date', 'certificate_number']
        labels = {
            'trainee': 'Trainee',
            'course': 'Course',
            'issue_date': 'Issue Date',
            'certificate_number': 'Certificate Number',
        }
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }
        placeholders = {
            'trainee': 'Select a trainee',
            'course': 'Select a course',
            'issue_date': 'Select issue date',
            'certificate_number': 'Enter certificate number',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.placeholders.get(field_name, '')
