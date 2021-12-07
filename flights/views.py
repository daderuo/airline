from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from  django.urls import  reverse
from django.http import HttpResponse,HttpResponseRedirect

from .models import Flight, Passenger

# Create your views here.

def index(request):
    #return HttpResponse("ciao")
    return render(request,"flights/index.html",{
        "Flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404

    passengers = flight.passenger.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))



