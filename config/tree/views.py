from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Person



def index(request):
    filtered = Person.objects.select_related('parent').order_by('level')

    paginator = Paginator(filtered, 1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main_page.html', {'page_obj': page_obj})

def current_person(request, pk):
    object = get_object_or_404(Person, pk=pk)
    return render(request, 'current.html', {'person': object})

