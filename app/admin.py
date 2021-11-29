from django.contrib import admin
from .models import Incident
@admin.register(Incident)
class Incidentadmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'incident_department', 'date_incident', 'time_incident', 'incident_location', 'initial_severity', 'suspected_cause', 'immediateaction_taken', 'subincident_types', 'reported_by']