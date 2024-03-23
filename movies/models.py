from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    fio = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    length = models.TimeField()
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
