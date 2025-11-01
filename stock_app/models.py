from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='phones/', blank=True, null=True)  # ← upload dans media/phones/
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name}"
