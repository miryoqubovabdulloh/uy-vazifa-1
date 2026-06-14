from django.shortcuts import render

# Create your views here.
def templatemo(request):
    return render(request, 'index.html')

def work(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')
