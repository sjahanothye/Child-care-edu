from django.contrib import admin
from .models import Parents, Child, Doctor, Schedule, LearningPlan, Consultation, HealthInfo

admin.site.register(Parents)
admin.site.register(Child)
admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(LearningPlan)
admin.site.register(Consultation)
admin.site.register(HealthInfo)

