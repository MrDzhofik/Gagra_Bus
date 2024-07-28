from django.contrib import admin
from .models import Route, Town, Stop, Route_Stop, Schedule

# Register your models here.
admin.site.register(Town)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Route_Stop)
admin.site.register(Schedule)
