from django.shortcuts import render

def home(request):
    return render(request, 'todo_list/home.html', {})

def about(request):
    return render(request, 'todo_list/about.html', {})
