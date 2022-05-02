from contextlib import nullcontext
from email.policy import default
from pyexpat import model
from random import choices
from click import option
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField
from jinja2 import ChainableUndefined
from stripe import max_network_retries

# PATIENT


class Patient(models.Model):

    GENDER = (
        ('Female', 'F'),
        ('Male', 'M'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# SUPPORT
OPTION = (
    ("It happened to me", "It happened to me"),
    ("It's already been like that", "It's already been like that"),
)

REASON = (
    ("Delete patient", "Delete patient"),
    ("System problems", "System problems"),
    ("Other", "Others"),
)

SITUATION = (
    ("Done", "Done"),
    ("Pending", "Pending"),
)


class Call(models.Model):
    terms = models.BooleanField("You got this resposibility")
    user = models.CharField(max_length=100)
    message = models.TextField()
    option = models.CharField(max_length=100, choices=OPTION)
    reason = models.CharField(max_length=100, choices=REASON)
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(
        max_length=100, null=True, choices=SITUATION, default='Pending')

    def __str__(self):
        return self.user
