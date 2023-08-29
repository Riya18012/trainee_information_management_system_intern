from django.db import models

# Create your models here.


class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Trainee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class TrainingCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Enrollment(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    training_period = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.trainee} - {self.course}"


class Certificate(models.Model):
    trainee = models.ForeignKey('Trainee', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    issue_date = models.DateField()
    certificate_number = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.trainee} - {self.course} Certificate"

