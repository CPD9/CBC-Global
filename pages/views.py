from django.shortcuts import render
from django.http import HttpResponse
# from projects.choices import state_choices

from projects.models import Project
from certificates.models import Certificate


def index(request):
    # projects = project.objects.order_by(
    #     '-list_date').filter(is_published=True)[:3]

    # context = {
    #     'projects': projects,
    #     # 'state_choices': state_choices,
    # }

    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def about(request):
    # Get all certificates
    certificates = Certificate.objects.order_by('hire_date')

    # Get MVP
    mvp_certificates = Certificate.objects.all().filter(is_mvp=True)

    context = {
        'certificates': certificates,
        'mvp_certificates': mvp_certificates
    }

    return render(request, 'pages/about.html')
