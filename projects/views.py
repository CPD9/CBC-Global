from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import state_choices, type_choices


from .models import Project


def index(request):
    projects = Project.objects.order_by('-list_date')

    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)

    context = {
        'projects': paged_projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    project = get_object_or_404(project, pk=project_id)

    context = {
        'project': project
    }

    return render(request, 'projects/project.html', context)


def search(request):
    queryset_list = project.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Types
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset_list = queryset_list.filter(type__iexact=type)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'type_choices': type_choices,
        'price_choices': price_choices,
        'projects': queryset_list,
        'values': request.GET
    }

    return render(request, 'projects/search.html', context)
