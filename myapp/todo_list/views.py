from django.shortcuts import render

def home(request):
    return render(request, 'todo_list/home.html', {})

def about(request):
    context = {
        'first_name': 'Yolla',
        'last_name': 'Ifliandry',
    }
    return render(request, 'todo_list/about.html', context)
