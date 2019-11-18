from django.shortcuts import render
from django.views.generic.base import TemplateView
from exams.models import Exam


class HomeView(TemplateView):
    template_name = "HomeView/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["exams"] = Exam.objects.all()
        return context
