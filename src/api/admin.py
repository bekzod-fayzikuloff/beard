from django.contrib import admin
from .models import Beard


@admin.register(Beard)
class BeardAdmin(admin.ModelAdmin):
    pass

