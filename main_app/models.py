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
    directions = models.CharField(max_length=500)
    altitude = models.FloatField()
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


INT_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),

)


class Review(models.Model):
    date = models.DateField(default=date.today)
    content = models.TextField(max_length=250)
    rating = models.IntegerField(
        default=5,
        choices=INT_CHOICES
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for hike_id: {self.hike_id} @{self.url}"


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    hikes = models.ManyToManyField(Hike)
