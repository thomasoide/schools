from django.shortcuts import render
from django.http import HttpResponse
from district_search.models import Districts

# Create your views here.

def index(request):
    error=False
    district_list = Districts.objects.order_by('district_name').values('district_name').distinct()
    return render(request, 'district_search/index.html', {'district_list': district_list})

def search(request):
    error=False
    if 'district' in request.GET:
        district_query = request.GET['district']
        if len(district_query) == 0:
            error = True
        else:
            suspension_list = Districts.objects.filter(district_name__search=district_query).order_by('district_name', 'school_year')
            district_list = Districts.objects.order_by('district_name').values('district_name').distinct()
            return render(request, 'district_search/results.html', {'suspension_list': suspension_list, 'district_query': district_query, 'district_list': district_list})
    return render(request, 'district_search/results.html', {'error': error})
