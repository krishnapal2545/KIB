from django.shortcuts import render

def home(request):
    return render(request,'KIB-homepage.html')