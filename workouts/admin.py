from django.contrib import admin
from .models import Exercise,Workout,User,Split
# Register your models here.

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(User)
admin.site.register(Split)