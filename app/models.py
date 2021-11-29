from django.db import models

# Create your models here.
class Incident(models.Model):
    location = models.CharField(max_length=200)
    incident_department = models.CharField(max_length=100)
    date_incident = models.DateField(auto_now_add=True)
    time_incident = models.TimeField(auto_now_add=True)
    incident_location = models.CharField(max_length=100)
    initial_severity = models.CharField(max_length=100)
    suspected_cause = models.TextField(max_length=150)
    immediateaction_taken = models.TextField(max_length=150)
    subincident_types = models.CharField(max_length=100)
    reported_by = models.CharField(max_length=100)