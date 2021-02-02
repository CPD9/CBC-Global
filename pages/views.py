from django.shortcuts import render
from django.http import HttpResponse
from projects.choices import state_choices, type_con_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from projects.models import Project
from certificates.models import Certificate


def index(request):
    projects = Project.objects.order_by('-list_date').filter()


    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)

    context = {
        'projects': projects,
        'projects': paged_projects,
        'state_choices': state_choices,
        'type_con_choices': type_con_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all certificates
    certificates = Certificate.objects.order_by('-hire_date')

    # Get MVP
    mvp_certificates = Certificate.objects.all().filter(is_mvp=True)

    paginator = Paginator(certificates, 6)
    page = request.GET.get('page')
    paged_certificates = paginator.get_page(page)

    context = {
        'certificates': certificates,
        'mvp_certificates': mvp_certificates,
        'certificates': paged_certificates
    }

    
    return render(request, 'pages/about.html', context)
