from django import forms
from .models import Child
from .models import HealthInfo, Consultation

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['Childname', 'ChildId', 'ParentsId', 'ChildCertificate', 'BrithDate']
exclude = ['BrithDate']

class HealthInfoForm(forms.ModelForm):
    class Meta:
        model = HealthInfo
        fields = ['ChildId', 'Vaccination', 'Allergies', 'MedicalCondition', 'CheckupDate']
        widgets = {
            'ChildId': forms.HiddenInput(),  # Hide this field
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['ChildId', 'ConsultationDate', 'ConsultationTime', 'Notes']
        widgets = {
            'ChildId': forms.HiddenInput(),  # Hide this field
        }
