from django.shortcuts import render

# Create your views here.

def gaming(request):
    return render(request, "gaming.html")
