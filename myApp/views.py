from django.shortcuts import render
from .models import MyModel


def model_list(request):
    models = MyModel.objects.all()
    return render(request, 'model_list.html', {'models': models})
