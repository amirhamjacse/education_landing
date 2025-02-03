from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView
from django.shortcuts import render
from .models import StudentsInformation, TeacherInfo, DetailsOfTeacher
from .forms import StudentInfoForm
from django.contrib import messages

# this class is for Landing page
class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        teacher = TeacherInfo.objects.all().order_by('sort')
        context = self.get_context_data(**kwargs)
        context['teachers'] = teacher
        return self.render_to_response(context)


# Registration View
class RegistrationView(View):
    template='registration_page.html'

    def get(self, request):
        forms = StudentInfoForm
        context = {
            'form': forms,
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student information saved successfully!")
            form = StudentInfoForm()
            context = {'form': form}
            return render(request, 'success_page.html', context)
        else:
            messages.error(request, "Please correct the errors below.")
        context = {'form': form}
        return render(request, self.template, context)



class TeacherDetailView(DetailView):
    model = TeacherInfo
    template_name = 'teacher_detail.html'  # Specify the template for displaying the details

    def get(self, request, *args, **kwargs):
        teacher_details = DetailsOfTeacher.objects.filter(teacher_id=self.kwargs['pk']).last()
        context = {
            'teacher_details': teacher_details,
        }
        return render(request, self.template_name, context)


import openpyxl
from django.http import HttpResponse
from .models import StudentsInformation

def export_students(request):
    # Fetch all student records
    students = StudentsInformation.objects.all()

    # Create a new workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Students"

    # Define the headers
    headers = [
        'First Name', 
        'Last Name', 
        'Father\'s Name', 
        'Mother\'s Name', 
        'Phone Number', 
        'School', 
        'District', 
        'Thana', 
        'Upazila', 
        'Email Address', 
        'Has Computer/Laptop'
    ]
    ws.append(headers)

    # Write student data to the worksheet
    for student in students:
        row = [
            student.first_name,
            student.last_name,
            student.fathers_name,
            student.mothers_name,
            student.phone_number,
            student.school,
            student.district,
            student.thana,
            student.upazila,
            student.email_address,
            student.has_computer_laptop
        ]
        ws.append(row)

    # Set up the response for the Excel file
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    # Save the workbook to the response object
    wb.save(response)
    return response


