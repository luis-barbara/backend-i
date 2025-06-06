# Generated by Django 5.1.7 on 2025-03-27 20:47

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                (
                    "skin",
                    models.CharField(
                        choices=[
                            ("LT", "Light"),
                            ("MD", "Medium"),
                            ("DR", "Dark"),
                            ("VL", "Very Light"),
                            ("VD", "Very Dark"),
                            ("OL", "Olive"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ethnicity",
                    models.CharField(
                        choices=[
                            ("WH", "White"),
                            ("BL", "Black"),
                            ("LA", "Latino/Hispanic"),
                            ("EA", "East Asian"),
                            ("SA", "South Asian"),
                            ("ME", "Middle Eastern"),
                            ("IN", "Indigenous"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "eye_color",
                    models.CharField(
                        choices=[
                            ("BR", "Brown"),
                            ("BL", "Blue"),
                            ("GR", "Green"),
                            ("HA", "Hazel"),
                            ("AM", "Amber"),
                            ("GY", "Gray"),
                            ("VI", "Violet"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "hair_color",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "hair_style",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "clothing",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "clothing_style",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "accessories",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "expression",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "pose",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_type",
                    models.CharField(
                        choices=[
                            ("PR", "Photorealistic"),
                            ("CT", "Cartoon"),
                            ("SK", "Sketch"),
                            ("PA", "Painting"),
                            ("3D", "3D Render"),
                            ("AB", "Abstract"),
                            ("CG", "Concept Art"),
                            ("IM", "Illustration"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_style",
                    models.CharField(
                        choices=[
                            ("RL", "Realistic"),
                            ("CT", "Cartoonish"),
                            ("AB", "Abstract"),
                            ("PA", "Painting"),
                            ("3D", "3D Render"),
                            ("AN", "Anime"),
                            ("SK", "Sketch"),
                            ("CG", "Concept Art"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_texture",
                    models.CharField(
                        choices=[
                            ("SM", "Smooth"),
                            ("RF", "Rough"),
                            ("GR", "Grainy"),
                            ("SM_RF", "Smooth and Rough"),
                            ("SM_GR", "Smooth and Grainy"),
                            ("RF_GR", "Rough and Grainy"),
                            ("SM_RF_GR", "Smooth, Rough and Grainy"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_dominant_colors",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_contrast",
                    models.CharField(
                        choices=[
                            ("VH", "Very High"),
                            ("HI", "High"),
                            ("MD", "Moderate"),
                            ("LO", "Low"),
                            ("VL", "Very Low"),
                            ("NO", "None"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_shading",
                    models.CharField(
                        choices=[
                            ("SO", "Soft"),
                            ("MO", "Moderate"),
                            ("HR", "Harsh"),
                            ("DR", "Dramatic"),
                            ("NO", "None"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_lighting",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image_additional_details",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=10,
                    ),
                ),
                ("image_url", models.URLField(blank=True, max_length=1024, null=True)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="characters",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Character",
                "verbose_name_plural": "Characters",
                "db_table": "characters",
            },
        ),
    ]
