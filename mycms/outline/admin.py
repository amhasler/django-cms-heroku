from models import Outline
from django.contrib import admin

class OutlineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Outline, OutlineAdmin)
