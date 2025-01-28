from django.db import models

# Create your models here.

class StudentsInformation(models.Model):
    name = models.CharField(
        max_length=255, blank=True, null=True
    )
    fathers_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    mothers_name = models.CharField(
        max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.name or "Unnamed Student"
