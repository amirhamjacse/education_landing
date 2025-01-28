from django import forms
from .models import StudentsInformation

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentsInformation
        fields = (
            # 'name',
            # 'fathers_name',
            # 'mothers_name',
            )
