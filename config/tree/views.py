from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .forms import PersonForm

def index(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Норм')
    return render(request, "base.html", {'form': form})

