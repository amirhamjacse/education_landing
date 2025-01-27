from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render
# Create your views here.


class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class RegistrationView(View):
    template='registration_page.html'

    def get(self, request):
        return render(request, self.template)