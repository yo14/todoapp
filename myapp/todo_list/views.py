from django.shortcuts import render
from .models import List
from .forms import ListForm

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'todo_list/home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todo_list/home.html', {'all_items': all_items})

def about(request):
    context = {
        'first_name': 'Yolla',
        'last_name': 'Ifliandry',
    }
    return render(request, 'todo_list/about.html', context)
