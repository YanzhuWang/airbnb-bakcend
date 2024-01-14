from django.db import models

from users.models import User


# Create your models here.
class House(models.Model):
    """Model representing House"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Is this a pet allowed?")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
