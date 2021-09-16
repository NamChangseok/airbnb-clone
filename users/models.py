from django.contrib.auth.models import AbstractUser
from django.db import models


# 이 모델을 장고에 연걸해야함

# Create your models here.


class User(AbstractUser):  # user을 장고의 user으로 가져옴

    """Custom User Model"""

    gender_male = "male"
    gender_female = "female"
    gender_other = "other"

    gender_choices = (
        (gender_male, "male"),
        (gender_female, "female"),
        (gender_other, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    Language_choices = (
        (LANGUAGE_ENGLISH, "english"),
        (LANGUAGE_KOREAN, "korean"),
    )

    currency_usd = "usd"
    currency_krw = "krw"

    currency_choices = (
        (currency_usd, "usd"),
        (currency_krw, "krw"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=10, null=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=Language_choices, max_length=2, blank=True)
    currency = models.CharField(choices=currency_choices, max_length=10, blank=True)
    superhost = models.BooleanField(default=True)
