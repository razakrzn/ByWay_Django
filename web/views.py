from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  


def details(request):
    return render(request, 'details.html')