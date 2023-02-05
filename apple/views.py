from django.shortcuts import render
from apple.models import predictions
from django.views.generic import View


# Create your views here.


def home_view(request):

    return render(request, 'homepage.html')


def post(request):

    company = str(request.POST.get("company-names")).lower()

    final_date = request.POST["date1"]
    price = predictions.objects.filter(date=final_date)

    for x in price:
        pred = getattr(x, company)

    return render(request, 'results.html', {'price': pred})


def back_view(request):
    return render(request, 'homepage.html')
