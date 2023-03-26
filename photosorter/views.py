from django.views.generic import TemplateView
from django.shortcuts import render
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        data = {}
        return render(request, 'index.html', data)
