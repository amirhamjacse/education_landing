from django import forms
from .models import StudentsInformation

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentsInformation
        fields = (
            'first_name',
            'last_name',
            # 'fathers_name',
            # 'mothers_name',
            'phone_number',
            'school',
            'district',
            'iam_student',
            'iam_gurdian',
            'gurdian_phone_number',
            # 'thana',
            'upazila',
            'email_address',
            'can_manage_laptop',
            'has_computer_laptop',
            )
