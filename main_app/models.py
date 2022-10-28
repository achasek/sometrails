from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

# Create your models here.

DIFFICULTY = (
    ('E', 'Easy'),
    ('M', 'Moderate'),
    ('D', 'Difficult'),
)


class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    date = models.DateField(default=date.today)
    content = models.TextField(max_length=250)
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']