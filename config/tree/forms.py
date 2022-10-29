from .models import Person
from django.forms import ModelForm


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = "__all__"

