from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    class LanguageChoices(models.TextChoices):
        KR = 'ko', 'Korean'
        EN = 'en', 'English'

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "US Dollar"
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    avatar = models.ImageField(null=True)
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default=GenderChoices.MALE)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)

