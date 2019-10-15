from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<p>Bonjour</p>')
    return render(request,'index.html')