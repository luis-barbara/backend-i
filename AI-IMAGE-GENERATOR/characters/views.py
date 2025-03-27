from django.shortcuts import redirect, render 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages  
from characters.forms import CharacterForm  
from characters.image_service import generate_image
from characters.models import Character


# View for the homepage
class IndexView(TemplateView):
    http_method_names=["get"]
    template_name="characters/index.html"

# View for user registration
class SignupView(FormView):
    template_name = "registration/signup.html"
    success_url = "/signin"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")



# View for character creation
class CreateCharacterView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/create_character.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Character.objects.filter(user=self.request.user).all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user  
        character = form.save(commit=False)

        # Generate the prompt based on the character's attributes
        prompt = f"""
        Create a highly detailed {character.get_image_type_display()} character portrait in {character.get_image_style_display()} style. 

        ### **Character Details:**
        - **Age/Gender:** {character.age}-year-old {character.get_gender_display()}
        - **Ethnicity/Skin:** {character.get_ethnicity_display()} with {character.get_skin_display()} skin tone
        - **Eyes/Hair:** Striking {character.get_eye_color_display()} eyes and {character.get_hair_style_display().lower()} {character.get_hair_color_display()} hair

        ### **Outfit & Style:**
        - **Clothing:** {character.get_clothing_display()} ({character.get_clothing_style_display()} style)
        - **Accessories:** {character.get_accessories_display()}
        - **Expression:** {character.get_expression_display().lower()}, confident demeanor
        - **Pose:** {character.get_pose_display().lower()}

        ### **Rendering Specs:**
        - **Lighting:** {character.get_image_lighting_display().lower()} 
        - **Shading:** {character.get_image_shading_display().lower()} shadows
        - **Texture:** {character.get_image_texture_display().lower()} texture
        - **Color Theme:** Dominant {character.get_image_dominant_colors_display().lower()} tones
        - **Background:** {character.get_image_additional_details_display().lower()}

        ### **Quality Requirements (DALL-E 3 Specific):**
        - Ultra HD, 8K resolution 
        - Studio lighting, professional artwork
        - Symmetrical, anatomically correct features
        - Highly detailed textures (skin, hair, fabric)
        - Coherent shadows and highlights
        - Style consistency: {character.get_image_style_display()}
        """

        try:
            image_url = generate_image(prompt)  
            if image_url:
                character.image_url = image_url
                character.save()
                messages.success(self.request, "Character created successfully!")
                return self.render_to_response(self.get_context_data(form=form, new_character=character))
            else:
                messages.error(self.request, "Image generation failed. Try again.")
                return render(self.request, self.template_name, self.get_context_data(form=form))

        except Exception as e:
            messages.error(self.request, f"Failed to generate image: {str(e)}")
            return render(self.request, self.template_name, self.get_context_data(form=form))
