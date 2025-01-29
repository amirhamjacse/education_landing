from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render
from .models import StudentsInformation
from .forms import StudentInfoForm
from django.contrib import messages

# this class is for Landing page
class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
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
            return render(request, self.template, context)
        else:
            messages.error(request, "Please correct the errors below.")

        context = {'form': form}
        return render(request, self.template, context)

    # def post(self, request):
    #     form = StudentInfoForm(request.POST)
    #     print(form, 'working form data ')
    #     if form.is_valid():
    #         form.save()
    #     # StudentsInformation
    #     forms = StudentInfoForm
    #     context = {
    #         'form': forms,
    #     }
    #     return render(request, self.template, context)
