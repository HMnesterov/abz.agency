from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Person



def index(request):
    filtered = Person.objects.all().order_by('level')
    return render(request, 'base.html', {'objects': filtered})

def current_person(request, pk):
    object = get_object_or_404(Person, pk=pk)
    return render(request, 'current.html', {'person': object})

