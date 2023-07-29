from django.shortcuts import render

# Create your views here.

def candidatos(request):
    return render(request, 'fantasy/index.html')