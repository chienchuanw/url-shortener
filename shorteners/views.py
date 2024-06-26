from django.shortcuts import render
from django.views.generic import TemplateView


class ShortenerHomeView(TemplateView):
    template_name = "shorteners/shortener_home.html"
