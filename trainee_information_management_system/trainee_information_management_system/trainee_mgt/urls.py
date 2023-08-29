from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("about/", views.About, name="about"),
    path('contact/',views.Contact, name='contact'),
    path('admin_login/', views.Login, name='admin_login'),
    path('logout/', views.Logout_admin, name='logout_admin'),
    path('index/', views.Index, name='dashboard'),
    path('certificate_list/', views.certificate_list, name='certificate_list'),
    path('trainee_list/', views.trainee_list, name='trainee_list'),
    path('training_center_list/', views.training_center_list, name='training_center_list'),
    path('enrollment_list/', views.enrollment_list, name='enrollment_list'),
    path('trainer_list/', views.trainer_list, name='trainer_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_trainee/', views.add_trainee, name='add_trainee'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('add_training_center/', views.add_training_center, name='add_training_center'),
    path('add_enrollment/', views.add_enrollment, name='add_enrollment'),
    path('add_certificate/', views.add_certificate, name='add_certificate'),
]
