from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('registration/', views.RegistrationView.as_view(), name='registration_page'),
    path('export/students/', views.export_students, name='export_students'),
]
