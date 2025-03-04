from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {"customers": customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/customer_detail.html', {"customer": customer})

def customer_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")  # Исправлена опечатка
        customer = Customer.objects.create(name=name, phone=phone)
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})
