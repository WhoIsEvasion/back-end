from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Reservation
from customers.models import Customer
from tables.models import Table

def reservation_create(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        table_id = request.POST.get("table_id")
        date = request.POST.get("date")

        customer = get_object_or_404(Customer, id=customer_id)
        table = get_object_or_404(Table, id=table_id)

    if Reservation.object.filter(customer=customer, date=date).exists():
        return JsonResponse({"error":"У вас уже есть бронь на этот день"}, status=400)

    if Reservation.object.filter(table=table, date=date).exists():
        return JsonResponse({"error":"Этот столик уже забронирован"}, status=400)

    reservation = Reservation.objects.create(customer=customer, table=table, date=date)
    return JsonResponse({"id":reservation.id, "status":reservation.status})

def reservation_detail(request,id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/reservation_detail.html', {'reservation':reservation})


def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer_id=user_id)
    return render(request, 'reservations/user_reservations.html', {"reservations":reservations})


def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        status = request.POST.get("status")
        if status in ["pending", "conirmed", "canceled"]:
            reservation.status = status
            reservation.saave()
            return JsonResponse({"id":reservation.id, "status":reservation.status})
        return JsonResponse({"error":"Неверный статус"}, status=400)


def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return JsonResponse({"message":"Бронь удалена"})