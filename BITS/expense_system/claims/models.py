from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Centre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ExpenseClaim(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Claim {self.id} by {self.employee.username}"

class ClaimItem(models.Model):
    claim = models.ForeignKey(ExpenseClaim, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')

    def __str__(self):
        return f"Item {self.id} for Claim {self.claim.id} - {self.description} - {self.amount}"