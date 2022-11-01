from django.contrib import admin
from .models import Hike, Review, Photo, Profile

# Register your models here.
admin.site.register(Hike)
admin.site.register(Review)
admin.site.register(Photo)
admin.site.register(Profile)
