from django.db import models

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name="reservations")
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE, related_name="reservations")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
