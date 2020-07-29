from django.shortcuts import render
from .models import List

def home(request):
    all_items = List.objects.all
    return render(request, 'todo_list/home.html', {'all_items':all_items})

def about(request):
    context = {
        'first_name': 'Yolla',
        'last_name': 'Ifliandry',
    }
    return render(request, 'todo_list/about.html', context)
