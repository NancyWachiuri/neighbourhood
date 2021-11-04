from django.contrib import admin
from .models import NeighbourHood,Business,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Business)