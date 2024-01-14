from django.db import models

from common.models import CommonModel
from users.models import User


# Create your models here.
class Experience(CommonModel):
    country = models.CharField(max_length=50, default="United States")
    city = models.CharField(max_length=80, default="Madison, WI")
    name = models.CharField(max_length=250)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey("categories.Category",
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Perk(CommonModel):
    name = models.CharField(max_length=250)
    detail = models.CharField(max_length=250, blank=True, default='')
    explanation = models.TextField()

    def __str__(self):
        return self.name
