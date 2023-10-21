from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # This is a tuple
    list_display_links = ('id', 'title') # This is a tuple
    list_filter = ('realtor',) # This is a tuple
    list_editable = ('is_published',) # This is a tuple
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # This is a tuple
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)