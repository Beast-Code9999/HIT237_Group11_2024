from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'assignment2_app/index.html')