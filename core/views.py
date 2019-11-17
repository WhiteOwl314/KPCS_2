from django.shortcuts import render
from django.views import View


class HomeView(View):
    return render(request, "index.html")
