from email.policy import default
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    hod_email = models.EmailField()
    hod_ph = models.IntegerField()


class Freezing_time(models.Model):
    before_t = models.TimeField()
    after_t = models.TimeField()


class Venue(models.Model):
    place = models.CharField(max_length=100)
    controller = models.CharField(max_length=100)
    cont_ph = models.IntegerField()
    cont_email = models.EmailField()
    availability = models.DateTimeField(null=True, blank=True)


class Time_set(models.Model):
    preference = models.DateTimeField()
    exclusion = models.DateTimeField()


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN" , 'Admin'
        STAFF = "STAFF" , 'Staff'
        CONVENOR = "CONVENOR" , 'Convenor'
        CHAIRMAN = "CHAIRMAN" , 'Chairman'
        DIRECTOR = "DIRECTOR", 'Director'
    role = models.CharField(max_length=50, choices=Role.choices)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class work_schedule(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected")
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    start_td = models.DateTimeField()
    end_td = models.DateTimeField()
    admin_status = models.CharField(max_length=50,choices = STATUS_CHOICES,default="pending")

class meeting(models.Model):
    PRIORITY = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
    )
    title = models.CharField(max_length=100)
    desc = models.TextField()
    start_td = models.DateTimeField()
    end_td = models.DateTimeField()
    agenda = models.TextField()
    vunue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY)
    minutes = models.TextField()

class Participants(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected")
    )
    meeting_id = models.ForeignKey(meeting, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    responses = models.CharField(max_length=50,choices=STATUS_CHOICES,default="pending")
    rej_msg = models.TextField()