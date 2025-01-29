from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import RegexValidator


class StudentsInformation(models.Model):
    # Fields
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    mothers_name = models.CharField(max_length=255, blank=True, null=True)

    # Regex validation for Bangladeshi phone numbers
    # phone_regex = RegexValidator(
    #     regex=r'^\01[3-9]\d{8}$',
    #     message="Phone number must be in the format '+01XXXXXXXXX' and valid for Bangladeshi carriers."
    # )
    phone_regex = RegexValidator(
        regex=r'^01\d{9}$',  # Starts with 01, followed by exactly 9 digits (making the total 11 digits)
        message="Phone number must be in the format '01XXXXXXXXX' and be exactly 11 digits long."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=11,  # Length of '+8801XXXXXXXXX'
        blank=True,
        null=True
    )
    school = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    thana = models.CharField(max_length=255, blank=True, null=True)
    upazila = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    # Boolean field for computer/laptop ownership
    has_computer_laptop = models.BooleanField(default=False)

    # Function to return the full name
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    # String representation of the model
    def __str__(self):
        return self.full_name() or "Unnamed Student"


class TeacherInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    sort = models.CharField(max_length=255, blank=True, null=True)
    picture = models.FileField(upload_to='teachers/', null=True, blank=True)
    # tpicture = models.ImageField(upload_to='teacherspic/', null=True, blank=True)
    # picture = models.ImageField(, null=True, blank=True)  # Use ImageField
    other_info = models.CharField(max_length=255, blank=True, null=True)
    # phone_regex = RegexValidator(
    #     regex=r'^01\d{9}$',  # Starts with 01, followed by exactly 9 digits (making the total 11 digits)
    #     message="Phone number must be in the format '01XXXXXXXXX' and be exactly 11 digits long."
    # )
    # phone_number = models.CharField(
    #     validators=[phone_regex],
    #     max_length=11,  # Length of '+8801XXXXXXXXX'
    #     blank=True,
    #     null=True
    # )
