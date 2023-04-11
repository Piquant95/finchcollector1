from django.contrib import admin
from .models import State, Updates, Upgrade

# Register your models here.

admin.site.register(State)
admin.site.register(Updates)
admin.site.register(Upgrade)
