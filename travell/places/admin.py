# Import necessary modules
from django.contrib import admin
from places.models import *



class GalleryAdmin(admin.TabularInline):
    # Specify fields to display in the inline representation
    list_display = ('place_field','name', 'image')
    # Set the model for the inline
    model = Gallery

# Define the admin class for Place
class PlaceAdmin(admin.ModelAdmin):
    # Specify fields to display in the list view
    list_display = ('name', 'place_field', 'category')
    # Include the GalleryAdmin inline
    inlines = [GalleryAdmin]

# Register the Place model with the admin site using PlaceAdmin
admin.site.register(Place, PlaceAdmin)

# Register the Category model with the admin site
admin.site.register(Category)
