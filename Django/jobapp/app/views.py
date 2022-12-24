# Create your views here.
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

from app.models import JobPost

job_title = [
    "First job",
    "Second job",
    "Third job"
]
job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]


class TempClass:
    x = 5


def hello(request):
    list = ["alpha", "beta"]
    temp_class = TempClass()
    is_authenticated = False

    context = {"name": "Django", "age": 23, "first_list": list, "temp_object": temp_class,
               "is_authenticated": is_authenticated}

    return render(request, "app/hello.html", context)


def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('job_detail', args=(job_id,))
    #
    #     list_of_jobs += f"<li><a href='{detail_url}'> {j} </a> </li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # response_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(response_html)
        # context = {"job_title": job_title[id], "job_description": job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Page Not Found")
