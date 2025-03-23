from django.contrib import admin
from characters.models import Character

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):

    list_display = (
        'gender', 'age', 'skin_color', 'ethnicity', 'eye_color', 
        'hair_color', 'hair_style', 'clothes', 'clothing_style', 
        'expression', 'pose', 'additional_details', 'image_type', 'style'
    )
    
    list_editable = (
        'age', 'skin_color', 'ethnicity', 'eye_color', 'hair_color', 
        'hair_style', 'clothes', 'clothing_style', 'expression', 'pose'
    )
    
    # Sorting the list of characters (ordering by age)
    ordering = ('age',)  
    
    # Filters to be used in the sidebar (quick filters)
    list_filter = ('gender', 'ethnicity', 'eye_color', 'hair_color')
    
    # Fields to be included in the search bar
    search_fields = ('gender', 'age', 'ethnicity', 'eye_color', 'hair_color')
    
    # Layout for each field in the admin interface (sectioned display)
    fieldsets = (
        ('Personal Information', {
            'fields': ('gender', 'age', 'skin_color', 'ethnicity')
        }),
        ('Appearance', {
            'fields': ('eye_color', 'hair_color', 'hair_style', 'clothes', 'clothing_style')
        }),
        ('Expression and Pose', {
            'fields': ('expression', 'pose')
        }),
        ('Image Details', {
            'fields': ('image_type', 'style', 'texture', 'dominant_colors', 'contrast', 'shading')
        }),
        ('Additional Details', {
            'fields': ('additional_details',)
        })
    )
    
    # Filter horizontal for ManyToMany relationships (ensure accessories is ManyToManyField in your model)
    filter_horizontal = ('accessories',)  
    
    # `sortable_by` is not needed unless you want the ability to sort by those fields in the admin interface
    # sortable_by = ('age', 'ethnicity', 'eye_color')  


admin.site.register(Character, CharacterAdmin)