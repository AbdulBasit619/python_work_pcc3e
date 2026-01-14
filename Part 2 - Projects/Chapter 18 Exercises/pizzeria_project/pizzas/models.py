from django.db import models


# Create your models here.
class Pizza(models.Model):
    """A pizza on which to place the toppings."""

    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """A topping to place on a particular pizza."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"
