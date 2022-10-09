from django.contrib import admin
from .models import Palette, Photos, Style, Material

admin.site.register(Style)
admin.site.register(Material)
admin.site.register(Palette)
admin.site.register(Photos)
