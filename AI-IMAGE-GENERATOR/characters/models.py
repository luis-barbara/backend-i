from django.db import models

# Create your models here.


class Character(models.Model):
    # Choices for limited field input
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    ETHNICITY_CHOICES = [
        ('caucasian', 'Caucasian'),
        ('african_american', 'African American'),
        ('hispanic', 'Hispanic'),
        ('asian', 'Asian'),
        ('other', 'Other'),
    ]
    
    EYE_COLOR_CHOICES = [
        ('brown', 'Brown'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('hazel', 'Hazel'),
        ('other', 'Other'),
    ]
    
    HAIR_COLOR_CHOICES = [
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('blonde', 'Blonde'),
        ('red', 'Red'),
        ('other', 'Other'),
    ]
    
    HAIR_STYLE_CHOICES = [
        ('short', 'Short'),
        ('medium', 'Medium'),
        ('long', 'Long'),
        ('bald', 'Bald'),
        ('other', 'Other'),
    ]
    
    CLOTHING_STYLE_CHOICES = [
        ('casual', 'Casual'),
        ('formal', 'Formal'),
        ('sporty', 'Sporty'),
        ('other', 'Other'),
    ]
    
    ACCESSORIES_CHOICES = [
        ('wristwatch', 'Wristwatch'),
        ('sunglasses', 'Sunglasses'),
        ('hat', 'Hat'),
        ('earrings', 'Earrings'),
        ('bracelet', 'Bracelet'),
        ('other', 'Other'),
    ]
    
    LIGHTING_CHOICES = [
        ('soft_diffuse', 'Soft and Diffuse'),
        ('harsh', 'Harsh'),
        ('dramatic', 'Dramatic'),
        ('natural', 'Natural'),
        ('other', 'Other'),
    ]
    
    IMAGE_TYPE_CHOICES = [
        ('photorealistic', 'Photorealistic'),
        ('cartoon', 'Cartoon'),
        ('sketch', 'Sketch'),
        ('other', 'Other'),
    ]
    
    STYLE_CHOICES = [
        ('realistic', 'Realistic'),
        ('cartoonish', 'Cartoonish'),
        ('abstract', 'Abstract'),
        ('other', 'Other'),
    ]
    
    TEXTURE_CHOICES = [
        ('smooth', 'Smooth'),
        ('rough', 'Rough'),
        ('grainy', 'Grainy'),
        ('other', 'Other'),
    ]
    
    CONTRAST_CHOICES = [
        ('high', 'High'),
        ('moderate', 'Moderate'),
        ('low', 'Low'),
    ]
    
    SHADING_CHOICES = [
        ('soft', 'Soft'),
        ('harsh', 'Harsh'),
        ('none', 'None'),
    ]
    
    # Fields from Character Model
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True, blank=True)  
    skin = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50, choices=ETHNICITY_CHOICES)
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES)
    hair_color = models.CharField(max_length=50, choices=HAIR_COLOR_CHOICES)
    hair_style = models.CharField(max_length=50, choices=HAIR_STYLE_CHOICES)
    clothing = models.CharField(max_length=255)
    clothing_style = models.CharField(max_length=50, choices=CLOTHING_STYLE_CHOICES)
    accessories = models.JSONField(default=list)  
    expression = models.CharField(max_length=255, null=True, blank=True)  
    pose = models.CharField(max_length=255, null=True, blank=True) 
    lighting = models.CharField(max_length=50, choices=LIGHTING_CHOICES)
    additional_details = models.TextField(null=True, blank=True)  

    # Imag Details
    image_type = models.CharField(max_length=50, choices=IMAGE_TYPE_CHOICES)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    texture = models.CharField(max_length=50, choices=TEXTURE_CHOICES)
    dominant_colors = models.CharField(max_length=50, null=True, blank=True)  
    contrast = models.CharField(max_length=50, choices=CONTRAST_CHOICES)
    shading = models.CharField(max_length=50, choices=SHADING_CHOICES)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='characters', null=True)

    class Meta:
        db_table = "characters"  
        verbose_name = "Character"  
        verbose_name_plural = "Characters"  

