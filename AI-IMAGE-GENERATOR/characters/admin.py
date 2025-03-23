from django.contrib import admin
from characters.models import Character

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    # Fields to be displayed in the admin list view
    list_display = (
        "name", "gender", "age", "skin", "ethnicity", "eye_color", 
        "hair_color", "hair_style", "clothing_style", "expression", 
        "pose", "image_type", "style"
    )

    # Fields that can be edited directly in the list view
    list_editable = (
        "gender", "age", "skin", "ethnicity", "eye_color", "hair_color", 
        "hair_style", "clothing_style", "expression", "pose"
    )

    # Default ordering of the objects
    ordering = ("age", "name")

    # Sidebar filters
    list_filter = ("gender", "ethnicity", "eye_color", "hair_color", "clothing_style", "image_type")

    # Searchable fields in the admin
    search_fields = ("name", "gender", "ethnicity", "eye_color", "hair_color")

    # Field grouping for better visualization in the admin detail page
    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "gender", "age", "skin", "ethnicity")
        }),
        ("Appearance", {
            "fields": ("eye_color", "hair_color", "hair_style", "clothing_style")
        }),
        ("Expression and Pose", {
            "fields": ("expression", "pose")
        }),
        ("Image Details", {
            "fields": ("image_type", "style", "texture", "dominant_colors", "contrast", "shading")
        }),
        ("Additional Information", {
            "fields": ("additional_details",)
        }),
    )

    # Sorting options in the admin list view
    sortable_by = ("age", "ethnicity", "eye_color")



admin.site.register(Character, CharacterAdmin)