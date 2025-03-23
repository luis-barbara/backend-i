from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, FormView
from characters.forms import CharacterForm  
from characters.image_service import generate_image  

# View for the homepage
class IndexView(TemplateView):
    template_name = "characters/index.html"  

# View for user registration
class SignupView(FormView):
    template_name = "registration/signup.html"
    success_url = "/signin" 
    form_class = UserCreationForm  

    def form_valid(self, form):
        user = form.save()  
        login(self.request, user)  
        return super().form_valid(form) 

# View for user login
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "registration/login.html"  
    next_page = '/select-character'  

# View for character creation
@login_required
def create_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user  
            character.save()  

            # After saving, we generate the image using the character's attributes
            details = character.details_imagem  

            # Generate the prompt based on the character's attributes
            prompt = f"""
            Create a {details['image_type']} image of a {character.gender} aged {character.age} years, with {character.skin} skin,
            {character.eye_color} penetrating eyes, and {character.hair_color} {character.hair_style} hair. 
            They are wearing {character.clothing}, with accessories like {', '.join(character.accessories)}. 
            They have a {character.expression} expression and are {character.pose}. 
            The lighting is {character.lighting}, with shading {details['shading']} to highlight the contours of the face and clothing. 
            The background should be neutral, uncluttered, and minimalist to facilitate later cropping.
            The image style will be {details['style']} and {details['image_type']}.
            The texture is {details['texture']}, with a focus on the sharp details of the face and clothing. 
            The predominant colors are {details.get('dominant_colors', 'neutral')} and the image should have {details.get('contrast', 'moderate')} contrast.
            """

            # Call the function to generate the image using the DALL·E API or another service
            image_url = generate_image(prompt)  

            # Save the image URL to the character model
            character.image_url = image_url
            character.save()  

            # Render the page with the created character and the generated image
            return render(request, "characters/create_character.html", {
                'form': form,
                'character': character  
            })
    else:
        form = CharacterForm()

    return render(request, "characters/create_character.html", {'form': form})
