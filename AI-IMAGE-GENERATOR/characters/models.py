from django.utils.timezone import now
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


# Defining choices

# 1. Basic Choices for Character Attributes
GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]

SKIN_CHOICES = [
    ("LT", "Light"),
    ("MD", "Medium"),
    ("DR", "Dark"),
    ("VL", "Very Light"),
    ("VD", "Very Dark"),
    ("OL", "Olive"),
]

ETHNICITY_CHOICES = [
    ("WH", "White"),
    ("BL", "Black"),
    ("LA", "Latino/Hispanic"),
    ("EA", "East Asian"),
    ("SA", "South Asian"),
    ("ME", "Middle Eastern"),
    ("IN", "Indigenous"),
]

EYE_COLOR_CHOICES = [
    ("BR", "Brown"),
    ("BL", "Blue"),
    ("GR", "Green"),
    ("HA", "Hazel"),
    ("AM", "Amber"),
    ("GY", "Gray"),
    ("VI", "Violet"),
]

HAIR_COLOR_CHOICES = [
    ("BK", "Black"),
    ("BR", "Brown"),
    ("BL", "Blonde"),
    ("RD", "Red"),
    ("GY", "Gray"),
    ("WH", "White"),
    ("AU", "Auburn"),
    ("BU", "Blue"),
    ("GR", "Green"),
    ("PU", "Purple"),
    ("PI", "Pink"),
    ("SI", "Silver"),
]

HAIR_STYLE_CHOICES = [
    ("SH_WG", "Short and Well-Groomed"),
    ("SH_UN", "Short and Unkempt"),
    ("MD_WG", "Medium and Well-Groomed"),
    ("MD_UN", "Medium and Unkempt"),
    ("LN_WG", "Long and Well-Groomed"),
    ("LN_UN", "Long and Unkempt"),
    ("CU_WG", "Curly and Well-Groomed"),
    ("CU_UN", "Curly and Unkempt"),
    ("ST_WG", "Straight and Well-Groomed"),
    ("ST_UN", "Straight and Unkempt"),
    ("WI_WG", "Wavy and Well-Groomed"),
    ("WI_UN", "Wavy and Unkempt"),
    ("BU_WG", "Buzz Cut and Well-Groomed"),
    ("BU_UN", "Buzz Cut and Unkempt"),
    ("AF_WG", "Afro and Well-Groomed"),
    ("AF_UN", "Afro and Unkempt"),
    ("MO_WG", "Mullet and Well-Groomed"),
    ("MO_UN", "Mullet and Unkempt"),
]

CLOTHING_CHOICES = [
    ("LB_SJ_DJ", "Light Blue Shirt and Dark Jeans"),
    ("WB_SJ_LJ", "White Button-up Shirt and Light Jeans"),
    ("BL_SJ_DJ", "Black Shirt and Dark Jeans"),
    ("GR_T_SH_LJ", "Gray T-shirt and Light Jeans"),
    ("RD_SJ_BJ", "Red Shirt and Black Jeans"),
    ("BL_T_SH_DJ", "Blue T-shirt and Dark Jeans"),
    ("GR_HO_LJ", "Gray Hoodie and Light Jeans"),
    ("BL_HO_DJ", "Black Hoodie and Dark Jeans"),
    ("WH_DRS_LJ", "White Dress and Light Jeans"),
    ("FL_JKT_DJ", "Flannel Jacket and Dark Jeans"),
    ("WI_T_SH_LJ", "White T-shirt and Light Jeans"),
    ("GR_HO_BJ", "Gray Hoodie and Black Jeans"),
    ("NV_SJ_LJ", "Navy Shirt and Light Jeans"),
    ("BL_CJ_BJ", "Black Cardigan and Black Jeans"),
    ("RD_T_SH_LJ", "Red T-shirt and Light Jeans"),
]

CLOTHING_STYLE_CHOICES = [
    ("CA", "Casual"),
    ("FO", "Formal"),
    ("SP", "Sporty"),
    ("BU", "Business"),
    ("ST", "Streetwear"),
    ("BO", "Bohemian"),
    ("GO", "Gothic"),
    ("VI", "Vintage"),
    ("PU", "Punk"),
    ("EL", "Elegant"),
]

EXPRESSION_CHOICES = [
    ("CF", "Confident"),
    ("SM", "Smiling"),
    ("SO", "Serious"),
    ("AN", "Angry"),
    ("SA", "Sad"),
    ("NE", "Neutral"),
    ("FR", "Frightened"),
    ("EX", "Excited"),
    ("SU", "Surprised"),
    ("DI", "Disappointed"),
]

POSE_CHOICES = [
    ("FF_UP", "Facing Forward, Upright Posture"),
    ("FF_SL", "Facing Forward, Slight Lean"),
    ("SI", "Sitting"),
    ("ST", "Standing"),
    ("ST_RL", "Standing, Relaxed"),
    ("ST_HS", "Standing, Hands in Pockets"),
    ("LF", "Leaning Forward"),
    ("BF", "Bent Forward"),
    ("LS", "Leaning Sideways"),
    ("RF", "Reclining Forward"),
    ("BF_AR", "Bent Forward, Arms Resting"),
    ("TF", "Tightened Frame, Body Forward"),
]

ACCESSORIES_CHOICES = [
    ("WW_SG", "Wristwatch and Sunglasses"),
    ("HT_SG", "Hat and Sunglasses"),
    ("BR_WW", "Bracelet and Wristwatch"),
    ("EA_RNG", "Earrings and Ring"),
    ("WW_HT", "Wristwatch and Hat"),
    ("SC_WW", "Scarf and Wristwatch"),
    ("SG_BG", "Sunglasses and Bag"),
    ("TP_BU", "Tie and Belt"),
    ("BR_SC", "Bracelet and Scarf"),
    ("NC_WW", "Necklace and Wristwatch"),
    ("WW_EA", "Wristwatch and Earrings"),
    ("SG_EA", "Sunglasses and Earrings"),
    ("WW_BA", "Wristwatch and Bracelet"),
]


# 2. Image Style Settings Choices
IMAGE_TYPE_CHOICES = [
    ("PR", "Photorealistic"),
    ("CT", "Cartoon"),
    ("SK", "Sketch"),
    ("PA", "Painting"),
    ("3D", "3D Render"),
    ("AB", "Abstract"),
    ("CG", "Concept Art"),
    ("IM", "Illustration"),
]

IMAGE_STYLE_CHOICES = [
    ("RL", "Realistic"),
    ("CT", "Cartoonish"),
    ("AB", "Abstract"),
    ("PA", "Painting"),
    ("3D", "3D Render"),
    ("AN", "Anime"),
    ("SK", "Sketch"),
    ("CG", "Concept Art"),
]

IMAGE_TEXTURE_CHOICES = [
    ("SM", "Smooth"),
    ("RF", "Rough"),
    ("GR", "Grainy"),
    ("SM_RF", "Smooth and Rough"),
    ("SM_GR", "Smooth and Grainy"),
    ("RF_GR", "Rough and Grainy"),
    ("SM_RF_GR", "Smooth, Rough and Grainy"),
]

IMAGE_DOMINANT_COLORS_CHOICES = [
    ("NE", "Neutral"),
    ("RD", "Red"),
    ("BL", "Blue"),
    ("GR", "Green"),
    ("YL", "Yellow"),
    ("OR", "Orange"),
    ("PK", "Pink"),
    ("WT", "White"),
    ("BK", "Black"),
    ("GRD", "Gradient"),
    ("VIO", "Violet"),
    ("BRN", "Brown"),
    ("BE", "Beige"),
    ("CR", "Cream"),
    ("IV", "Ivory"),
]

IMAGE_CONTRAST_CHOICES = [
    ("VH", "Very High"),
    ("HI", "High"),
    ("MD", "Moderate"),
    ("LO", "Low"),
    ("VL", "Very Low"),
    ("NO", "None"),
]

IMAGE_SHADING_CHOICES = [
    ("SO", "Soft"),
    ("MO", "Moderate"),
    ("HR", "Harsh"),
    ("DR", "Dramatic"),
    ("NO", "None"),
]

# 3. Image Effects (Lighting and Additional Details)
IMAGE_LIGHTING_CHOICES = [
    ("SD", "Soft and Diffuse"),
    ("HR", "Harsh"),
    ("DR", "Dramatic"),
    ("NT", "Natural"),
    ("BC", "Backlit"),
    ("CL", "Cinematic"),
    ("MG", "Moody and Gloomy"),
    ("GD", "Golden Hour"),
    ("BL", "Blue Hour"),
    ("NE", "Neon Glow"),
]

IMAGE_ADDITIONAL_DETAILS_CHOICES = [
    ("NB_UR", "No Background, Ultra-realistic"),
    ("BG_NM", "Background, Night Mode"),
    ("BG_SF", "Background, Soft Focus"),
    ("NB_DR", "No Background, Dramatic Lighting"),
    ("BG_HD", "Background, High Definition"),
    ("NB_LD", "No Background, Low Detail"),
    ("BG_VS", "Background, Vintage Style"),
    ("NB_PS", "No Background, Pseudo-realistic"),
    ("BG_SV", "Background, Sepia Vibe"),
    ("NB_SF", "No Background, Soft Focus"),
    ("BG_CE", "Background, Cinematic Effect"),
]




# Character Model
class Character(models.Model):
    id = models.BigAutoField(primary_key=True)  

    # Basic Information
    title = models.CharField(max_length=255)  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) 
    age = models.PositiveIntegerField()  
    skin = models.CharField(max_length=10,choices=SKIN_CHOICES)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES)  

    # Physical Attributes
    eye_color = models.CharField(max_length=10, choices=EYE_COLOR_CHOICES)
    hair_color = models.CharField(max_length=10, choices=HAIR_COLOR_CHOICES)
    hair_style = models.CharField(max_length=10, choices=HAIR_STYLE_CHOICES)

    # Clothing and Accessories
    clothing = models.CharField(max_length=10,  choices=CLOTHING_CHOICES) 
    clothing_style = models.CharField(max_length=10, choices=CLOTHING_STYLE_CHOICES)
    accessories = models.CharField(max_length=10, choices=ACCESSORIES_CHOICES)

    # Expression and Pose
    expression = models.CharField(max_length=10, choices=EXPRESSION_CHOICES) 
    pose = models.CharField(max_length=10, choices=POSE_CHOICES) 

    # Image Style Settings
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
    image_style = models.CharField(max_length=10, choices=IMAGE_STYLE_CHOICES)
    image_texture = models.CharField(max_length=10, choices=IMAGE_TEXTURE_CHOICES)
    image_dominant_colors = models.CharField(max_length=10, choices=IMAGE_DOMINANT_COLORS_CHOICES) 
    image_contrast = models.CharField(max_length=10, choices=IMAGE_CONTRAST_CHOICES)
    image_shading = models.CharField(max_length=10, choices=IMAGE_SHADING_CHOICES)

    # Image Details
    image_lighting = models.CharField(max_length=10, choices=IMAGE_LIGHTING_CHOICES)
    image_additional_details = models.CharField(max_length=10, choices=IMAGE_ADDITIONAL_DETAILS_CHOICES) 

    

    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name="characters", null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    date = models.DateTimeField(default=now, blank=True)


    class Meta:
        db_table = "characters" 
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.title











