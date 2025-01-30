from django.contrib import admin
from .models import StudentsInformation
from .models import TeacherInfo
# Register your models here.
from import_export.admin import ExportMixin, ExportActionMixin


# @admin.register(StudentsInformation)
# class StudentsInformationAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = (
#             'first_name',
#             'last_name',
#             'fathers_name',
#             'mothers_name',
#             'phone_number',
#             'school',
#             'district',
#             'thana',
#             'upazila',
#             'email_address',
#             'has_computer_laptop',
#             )

#     search_fields = ('first_name',)
#     export_fields = ('first_name', 'last_name', 'fathers_name', 'mothers_name', 'phone_number')


@admin.register(TeacherInfo)
class TeacherInformationAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
                'name',
                'degree',
                'sort',
                'other_info',
            )



# from import_export import resources
# from django.contrib import admin
# from .models import StudentsInformation
# from import_export.admin import ExportActionMixin

# class StudentsInformationResource(resources.ModelResource):
#     class Meta:
#         model = StudentsInformation
#         fields = ('first_name', 'last_name', 'fathers_name', 'mothers_name', 'phone_number')
#         export_order = ('first_name', 'last_name', 'fathers_name', 'mothers_name', 'phone_number')

# class StudentsInformationAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = (
#         'first_name',
#         'last_name',
#         'fathers_name',
#         'mothers_name',
#         'phone_number',
#         'school',
#         'district',
#         'thana',
#         'upazila',
#         'email_address',
#         'has_computer_laptop',
#     )
#     search_fields = ('first_name',)
#     resource_class = StudentsInformationResource  # Using the custom resource

# admin.site.register(StudentsInformation, StudentsInformationAdmin)


import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import StudentsInformation


# Function to export students to an Excel file
def export_students(modeladmin, request, queryset):
    # Create a new workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Students"

    # Define the headers
    headers = [
        'First Name', 
        'Last Name', 
        # 'Father\'s Name', 
        # 'Mother\'s Name', 
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
            student.first_name,
            student.last_name,
            # student.fathers_name,
            # student.mothers_name,
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
        'first_name', 'last_name', 
        'phone_number', 'school', 'district', 'upazila', 
        'email_address', 'has_computer_laptop', 'can_manage_laptop',
    )
    search_fields = ('first_name',)
    
    # Define the export action
    actions = [export_students]
