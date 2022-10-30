from django.urls import path
from .views import index, current_person
urlpatterns = [
    path('', index, name='base'),
    path('person/<int:pk>', current_person, name='employee')

]