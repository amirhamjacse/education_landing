from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class LandingPageview(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
