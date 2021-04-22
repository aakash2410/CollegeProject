from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user_id = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,
        primary_key = True)
    mobile_number = models.IntegerField(default = 0)

    def __str__(self):
        return "{}".format(self.user_id)


spec = [
        ('Dentist', 'Dentist'),
        ('Cardiologitst','Cardiologitst'),
        ('Cosmetic', 'Cosmetic')
    ]
  
class Doctor(models.Model):
    user_id = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,
        primary_key = True)

    qualifiation = models.CharField(
        choices=spec,
        null = True, 
        blank=True, 
        max_length=30)

    mobile_number = models.IntegerField(default = 0)

    def __str__(self):
        return "{}".format(self.user_id)


class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_approved = models.BooleanField(null = True, blank = True)
    reason = models.TextField(max_length=1024, blank = True, null = True)
    prior_reports = models.ImageField()
    is_alerted = models.BooleanField(default = False)

    def __str__(self):
        return "{} {}".format(self.date, self.time)
