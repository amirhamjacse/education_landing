from django.contrib import admin
from .models import StudentsInformation
# Register your models here.

@admin.register(StudentsInformation)
class StudentsInformationAdmin(admin.ModelAdmin):
    list_display = (
            'first_name',
            'last_name',
            'fathers_name',
            'mothers_name',
            'phone_number',
            'school',
            'district',
            'thana',
            'upazila',
            'email_address',
            'has_computer_laptop',
            )

    search_fields = ('first_name',)