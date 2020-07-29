from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to list!'))
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

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')


