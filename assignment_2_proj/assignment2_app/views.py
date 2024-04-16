from django.shortcuts import render
from assignment2_app import classes
from . classes import members_list, projects_list # list of distionaries of projects

# print(projects_list)


# http://127.0.0.1:8000/
def home(request):
    return render(request, "assignment2_app/index.html")


# http://127.0.0.1:8000/project-details
def project_details(request, slug):
    context = {}

    return render(request, "assignment2_app/projectDetails.html", context)


# http://127.0.0.1:8000/project-list
def project_list(request):
    context = {
        "projects": projects_list
    }
    return render(request, "assignment2_app/projectList.html", context)


# http://127.0.0.1:8000/about
def about(request):
    # images = [
    #     {
    #         "title": "FB_IMG_1709708766525.jpg",
    #     },
    #     {
    #     "micia": "micia-pic.jpg",
    #     },
    # ]

    images = "FB_IMG_1709708766525.jpg"


    context = {
        "members": members_list,
        "images": images,
    }

    return render(request, "assignment2_app/about.html", context)
