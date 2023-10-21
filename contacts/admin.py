from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date') # This is a tuple
    list_display_links = ('id', 'name') # This is a tuple
    search_fields = ('name', 'email', 'listing') # This is a tuple
    list_per_page = 25

# Register your models here.
admin.site.register(Contact, ContactAdmin)