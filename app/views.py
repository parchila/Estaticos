from django.shortcuts import render

# Create your views here.
def vista1(request):
    return render(request, 'index.html')