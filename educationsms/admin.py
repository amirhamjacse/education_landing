import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import StudentsInformation
from .models import TeacherInfo, DetailsOfTeacher
# Register your models here.
from import_export.admin import ExportMixin, ExportActionMixin


@admin.register(TeacherInfo)
class TeacherInformationAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
                'name',
                'degree',
                'sort',
                'other_info',
            )


# Function to export students to an Excel file
def export_students(modeladmin, request, queryset):
    # Create a new workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Students"

    # Define the headers
    headers = [
        'iam_student',
        'iam_gurdian',
        'First Name', 
        'Last Name', 
        'gurdian_phone_number',
        'Phone Number', 
        'School', 
        'District', 
        # 'Thana', 
        'Upazila/Thana', 
        'Email Address', 
        'Has Computer/Laptop',
        'Can Manage Laptop/Computer',
    ]
    ws.append(headers)

    # Write student data to the worksheet
    for student in queryset:
        row = [
            'Yes' if student.iam_gurdian else 'No',
            'Yes' if student.iam_student else 'No',
            student.first_name,
            student.last_name,
            # student.fathers_name,
            student.gurdian_phone_number,
            student.phone_number,
            student.school,
            student.district,
            # student.thana,
            student.upazila,
            student.email_address,
            'Yes' if student.has_computer_laptop else 'No',  # Convert True/False to Yes/No
            'Yes' if student.can_manage_laptop else 'No'  # Convert True/False to Yes/No
        ]
        ws.append(row)

    # Set up the response for the Excel file
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=students_information.xlsx'

    # Save the workbook to the response object
    wb.save(response)
    return response


# Register the admin class with the custom export action
@admin.register(StudentsInformation)
class StudentsInformationAdmin(admin.ModelAdmin):
    list_display = (
        'iam_gurdian',
        'iam_student',
        'gurdian_phone_number','first_name', 'last_name', 
        'phone_number', 'school', 'district', 'upazila', 
        'email_address', 'has_computer_laptop', 'can_manage_laptop',
    )
    search_fields = ('first_name',)
    
    # Define the export action
    actions = [export_students]


@admin.register(DetailsOfTeacher)
class DetailsOfTeacherAdmin(admin.ModelAdmin):
    list_display = (
        'teacher',
        'works',
        'qualifications',
        'others',
            )

