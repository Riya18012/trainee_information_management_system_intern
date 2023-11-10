# trainee_information_management_system
To develop a Trainee Information Management System website using Django, HTML, and CSS technologies.
In the Trainee Information Management System project, several entities (database models) are defined to represent different aspects of the system. Here's a list of entities used in my project:-
# Trainee:
Attributes:
trainee_id (AutoField): Primary key for the Trainee model.
name (CharField): Name of the trainee.
age (PositiveIntegerField): Age of the trainee.
gender (CharField): Gender of the trainee (choices: male, female, other).
date_of_birth (DateField): Date of birth of the trainee.
phone_num (CharField): Phone number of the trainee.
address (TextField): Address of the trainee.
email (EmailField): Email address of the trainee.
course (ForeignKey to Course, nullable): Relationship with Course to associate trainees with specific courses.

# TrainingCenter:
Attributes:
id (AutoField): Primary key for the TrainingCenter model.
name (CharField): Name of the training center.
location (CharField): Location of the training center.
contact_email (EmailField): Email contact for the training center.

# Course:
Attributes:
id (AutoField): Primary key for the Course model.
name (CharField): Name of the course.
description (TextField): Description of the course.
training_center (ForeignKey to TrainingCenter): Relationship with TrainingCenter to associate courses with specific training centers.


# Trainer:
Attributes:
id (AutoField): Primary key for the Trainer model.
name (CharField): Name of the trainer.
specialization (CharField): Specialization or expertise of the trainer.
designation (CharField, nullable): Designation of the trainer.

# Enrollment:
Attributes:
id (AutoField): Primary key for the Enrollment model.
trainee (ForeignKey to Trainee): Relationship with Trainee to associate enrollments with specific trainees.
course (ForeignKey to Course): Relationship with Course to associate enrollments with specific courses.
enrollment_date (DateField): Date of enrollment.
training_period (PositiveIntegerField): Training period in months.
