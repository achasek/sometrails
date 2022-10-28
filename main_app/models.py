from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIFFICULTY = (
    ('E', 'Easy'),
    ('M', 'Moderate'),
    ('D', 'Difficult'),
)


class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_difficulty_display()}'