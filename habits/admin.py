from django.contrib import admin
from . models import Habit, HabitUpdate
# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitUpdate)
