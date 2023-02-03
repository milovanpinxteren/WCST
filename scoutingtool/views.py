from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'critereaselection.html')


# def login(request):
#     print('login')
#     return render('../templates/login.html')