from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

month_challenge = {
    "january": "Codechef 3 star",
    "february": "Codeforces Pupil",
    "march": "Leetcode Guardian",
    "april": "Django Course",
    "may": "DSA",
    "june": "Graph and DP",
    "july": "Codeforces Specilist",
    "august": "Get Placed",
    "september": "Codeforces CM",
    "october": "Build Physique",
    "november": "Get Internship",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(month_challenge.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(month_challenge.keys())
    if (month > len(months)):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = month_challenge[month]
        response_data = render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponse(response_data)
