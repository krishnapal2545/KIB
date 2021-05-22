from django.shortcuts import render

def loader(request):
    return render(request,'KIB-loader.html')

def home(request):
    return render(request,'KIB-homepage.html')