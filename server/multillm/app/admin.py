from django.contrib import admin
from .models import Prompt
# Register models here so they can appear inside of the admin panel (allowing us to modify/view them)
admin.site.register(Prompt)