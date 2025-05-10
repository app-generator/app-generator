from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Purchase(models.Model):
    user_id = models.IntegerField(default=-1)
    email = models.EmailField()
    purchase_id = models.CharField(max_length=255, unique=True)
    purchase_value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.purchase_id} - {self.email}"
