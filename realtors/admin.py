from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date') # This is a tuple
    list_display_links = ('id', 'name') # This is a tuple
    search_fields = ('name',) # This is a tuple
    list_per_page = 25

# Register your models here.
admin.site.register(Realtor, RealtorAdmin)