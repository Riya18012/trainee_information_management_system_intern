from django.contrib import admin

# Register your models here.
from .models import TrainingCenter, Course, Trainer, Trainee, Enrollment, Certificate

admin.site.register(TrainingCenter)
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Trainee)
admin.site.register(Enrollment)
admin.site.register(Certificate)