from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    context = {}
    return TemplateResponse(request, "middleware_demo/index.html", context=context)