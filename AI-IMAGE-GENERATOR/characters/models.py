from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


# Defining choices 
GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

ETHNICITY_CHOICES = [
    ("CA", "Caucasian"),
    ("AA", "African American"),
    ("HI", "Hispanic"),
    ("AS", "Asian"),
    ("OT", "Other"),
]

EYE_COLOR_CHOICES = [
    ("BR", "Brown"),
    ("BL", "Blue"),
    ("GR", "Green"),
    ("HA", "Hazel"),
    ("OT", "Other"),
]

HAIR_COLOR_CHOICES = [
    ("BK", "Black"),
    ("BR", "Brown"),
    ("BL", "Blonde"),
    ("RD", "Red"),
    ("OT", "Other"),
]

HAIR_STYLE_CHOICES = [
    ("SH", "Short"),
    ("MD", "Medium"),
    ("LG", "Long"),
    ("BD", "Bald"),
    ("OT", "Other"),
]

CLOTHING_STYLE_CHOICES = [
    ("CA", "Casual"),
    ("FO", "Formal"),
    ("SP", "Sporty"),
    ("OT", "Other"),
]

ACCESSORIES_CHOICES = [
    ("WW", "Wristwatch"),
    ("SG", "Sunglasses"),
    ("HT", "Hat"),
    ("EA", "Earrings"),
    ("BR", "Bracelet"),
    ("OT", "Other"),
]

LIGHTING_CHOICES = [
    ("SD", "Soft and Diffuse"),
    ("HR", "Harsh"),
    ("DR", "Dramatic"),
    ("NT", "Natural"),
    ("OT", "Other"),
]

IMAGE_TYPE_CHOICES = [
    ("PR", "Photorealistic"),
    ("CT", "Cartoon"),
    ("SK", "Sketch"),
    ("OT", "Other"),
]

STYLE_CHOICES = [
    ("RL", "Realistic"),
    ("CT", "Cartoonish"),
    ("AB", "Abstract"),
    ("OT", "Other"),
]

TEXTURE_CHOICES = [
    ("SM", "Smooth"),
    ("RF", "Rough"),
    ("GR", "Grainy"),
    ("OT", "Other"),
]

CONTRAST_CHOICES = [
    ("HI", "High"),
    ("MD", "Moderate"),
    ("LO", "Low"),
]

SHADING_CHOICES = [
    ("SF", "Soft"),
    ("HR", "Harsh"),
    ("NO", "None"),
]

# Character Model
class Character(models.Model):
    id = models.BigAutoField(primary_key=True)  

    # Basic Information
    name = models.CharField(max_length=255)  
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    age = models.PositiveIntegerField()  
    skin = models.CharField(max_length=50)  
    ethnicity = models.CharField(max_length=2, choices=ETHNICITY_CHOICES)  

    # Physical Attributes
    eye_color = models.CharField(max_length=2, choices=EYE_COLOR_CHOICES)
    hair_color = models.CharField(max_length=2, choices=HAIR_COLOR_CHOICES)
    hair_style = models.CharField(max_length=2, choices=HAIR_STYLE_CHOICES)

    # Clothing and Accessories
    clothing = models.CharField(max_length=255)  
    clothing_style = models.CharField(max_length=2, choices=CLOTHING_STYLE_CHOICES)
    accessories = models.JSONField()  

    # Expression and Pose
    expression = models.CharField(max_length=255)  
    pose = models.CharField(max_length=255)  

    # Image Details
    lighting = models.CharField(max_length=2, choices=LIGHTING_CHOICES)
    additional_details = models.TextField()  

    # Image Style Settings
    image_type = models.CharField(max_length=2, choices=IMAGE_TYPE_CHOICES)
    style = models.CharField(max_length=2, choices=STYLE_CHOICES)
    texture = models.CharField(max_length=2, choices=TEXTURE_CHOICES)
    dominant_colors = models.CharField(max_length=50)  
    contrast = models.CharField(max_length=2, choices=CONTRAST_CHOICES)
    shading = models.CharField(max_length=2, choices=SHADING_CHOICES)

    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="characters", null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)  

    class Meta:
        db_table = "characters" 
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.name











