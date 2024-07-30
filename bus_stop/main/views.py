from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Route, Stop, Route_Stop, Schedule

# Create your views here.

def home(request):
    route = Route.objects.all().order_by("number")
    return render(request, 'main/main.html', context={'routes':route})

def show_route(request, route_id):
    route = Route.objects.get(id=route_id) # Получаем информацию о конкретном маршруте

    route_stops = Route_Stop.objects.filter(route=route) # Получаем остановки этого маршрута

    stops_and_times = []
    for route_stop in route_stops:
        stop_name = route_stop.stop.name
        stop_times = Schedule.objects.filter(route_stop=route_stop) # Получаем все времена прибытия по остановке
        times = [schedule.time for schedule in stop_times]
        stops_and_times.append({'stop_name': stop_name, 'times': times})
        

    context = {
        'route': route,
        'stops_and_times': stops_and_times
    }

    return render(request, 'main/route.html', context)
