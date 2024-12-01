from django.contrib import admin
from .models import Child, Consultation, Doctor, HealthInfo, LearningPlan, Parents, Schedule
# Register your models here.
admin.site.register([Child, Consultation, Doctor, HealthInfo, LearningPlan, Parents, Schedule])