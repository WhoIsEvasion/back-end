from django.shortcuts import render
from django.http import JsonResponse
from .models import Table

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/table_list.html', {'tables': tables}) 



def table_create(request):
    if request.method == "POST":
        number = request.POST.get("number")
        seats = request.POST.get("seats")
        table = Table.objects.create(number=number, seats=seats)
        return JsonResponse({"id":table.id, "number":table.number, "seats":table.seats, "is_available":table.is_available})

def available_tables(request):
    tables = Table.objects.filter(is_available=True)
    return render(reqeust, 'tables/availble_tables.html', {"tables":tables})
