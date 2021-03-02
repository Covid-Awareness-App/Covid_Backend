from django.contrib import admin
from .models import State, Location, Feedback

# Register your models here.

admin.site.register(State)
admin.site.register(Location)
admin.site.register(Feedback)