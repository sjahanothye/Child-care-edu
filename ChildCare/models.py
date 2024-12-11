from django.db import models


# Create your models here.
class Parents(models.Model):
    ParentsId = models.IntegerField(blank=True, null=True)
    ParentsNID = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=200)


    def __str__(self):
        return self.Name

class Child(models.Model):
    Childname = models.CharField(max_length=200)
    ChildId=models.IntegerField(blank=True, null=True)
    ParentsId=models.ForeignKey(Parents, on_delete=models.CASCADE, blank=True, null=True)
    ChildCertificate=models.ImageField(upload_to='certificate/')
    BrithDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Childname

class Doctor(models.Model):
    DoctorId = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=200)
    Specification = models.CharField(max_length=100)
    AvailableHours = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Schedule(models.Model):
    ScheduleId = models.IntegerField(blank=True, null=True)
    ChildId= models.ForeignKey(Child, on_delete=models.CASCADE)
    SchoolType=models.CharField(max_length=200)

    def __str__(self):
        return self.SchoolType

class LearningPlan(models.Model):
    PlanId=models.IntegerField(blank=True, null=True)
    ChildId = models.ForeignKey(Child, on_delete=models.CASCADE)
    PlanName=models.CharField(max_length=200)
    Descrption=models.TextField(blank=True, null=True)
    AgeGroup=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.PlanName

class Consultation(models.Model):
    ConsultationId=models.IntegerField(blank=True, null=True)
    ChildId = models.ForeignKey(Child, on_delete=models.CASCADE)
    ConsultationDate=models.DateTimeField(blank=True, null=True)
    ConsultationTime=models.TimeField(blank=True, null=True)
    Notes=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.ConsultationId)  # Convert integer to string


class HealthInfo(models.Model):
    HealthInfoId=models.IntegerField(blank=True, null=True)
    ChildId = models.ForeignKey(Child, on_delete=models.CASCADE)
    Vaccination=models.TextField(max_length=200)
    Allergies=models.TextField(max_length=200)
    MedicalCondition=models.CharField(max_length=200)
    CheckupDate=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.MedicalCondition

