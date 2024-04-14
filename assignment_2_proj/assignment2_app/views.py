from django.shortcuts import render
from assignment2_app import classes 

# http://127.0.0.1:8000/
def home(request):
    return render(request, 'assignment2_app/index.html')

# http://127.0.0.1:8000/project-details
def project_details(request):

    context = {

    }

    return render(request, "assignment2_app/projectDetails.html", context)


def project_list(request):

    context = {

    }

    return render(request, "assignment2_app/projectList.html", context)

def about(request):

    context = {

    }

    return render(request, "assignment2_app/about.html", context)