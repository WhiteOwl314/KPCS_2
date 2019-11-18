from django.db import models
from datetime import date
from django.utils import timezone


class Exam(models.Model):
    name = models.CharField(max_length=50)
    examDate = models.DateField(auto_now_add=False)
    receptionDate_created = models.DateField(auto_now_add=False)
    receptionDate_ended = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
