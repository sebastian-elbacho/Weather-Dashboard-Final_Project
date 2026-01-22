from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')                                                #HttpResponse("Weather Dashboard works! TEST ONE")


@login_required
def dashboard(request):
    return render(request, "weather/dashboard.html")
