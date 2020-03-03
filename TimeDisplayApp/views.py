from time import gmtime, strftime
from django.shortcuts import render
from django.shortcuts import render, redirect


def index(request):
    context = {
        "time1": strftime("%b %d %Y", gmtime()),
        "time2": strftime("%H:%M %p", gmtime()),
        "title": "The current time and date:",
    }
    return render(request, 'index.html', context)
