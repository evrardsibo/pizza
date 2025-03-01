from django.contrib import admin
from . import models

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vegetarian')
    list_filter = ('vegetarian',)
    search_fields = ('name', 'description')

admin.site.register(models.Pizza, PizzaAdmin)


