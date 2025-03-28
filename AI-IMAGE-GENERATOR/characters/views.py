from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages  
from characters.forms import CharacterForm  
from characters.image_service import generate_image
from characters.models import Character
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView



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
        Generate a {character.get_image_style_display().lower()} character portrait with strict adherence to these specifications:

        ### Physical Attributes:
        - {character.age}-year-old {character.get_gender_display().lower()}
        - Ethnicity: {character.get_ethnicity_display()}
        - Skin: {character.get_skin_display().lower()} tone
        - Eyes: {character.get_eye_color_display().lower()} (must match exactly)
        - Hair: {character.get_hair_style_display().lower()} {character.get_hair_color_display().lower()}

        ### Styling:
        - Outfit: {character.get_clothing_display()} ({character.get_clothing_style_display().lower()})
        - Accessories: {character.get_accessories_display().lower()}
        - Expression: {character.get_expression_display().lower()} 
        - Pose: {character.get_pose_display().lower()}

        ### Rendering Specifications:
        - Style: {character.get_image_style_display().lower()}
        - Lighting: {character.get_image_lighting_display().lower()}
        - Shading: {character.get_image_shading_display().lower()} shadows
        - Texture: {character.get_image_texture_display().lower()} surfaces
        - Colors: Dominant {character.get_image_dominant_colors_display().lower()} palette
        - Background: {character.get_image_additional_details_display().lower()}

        ### Photography Details:
        - Camera: {character.get_camera_display()} with {character.get_lens_display()}
        - Settings: ISO {character.get_iso_display()}, {character.get_exposure_display()} shutter

        ### Mandatory Requirements:
        1. Accuracy:
        - Eye color must be {character.get_eye_color_display().lower()} (no variations)
        - Skin tone must match "{character.get_skin_display().lower()}" exactly
        - Hair style/color as described
        2. Quality:
        - 8K resolution, studio lighting
        - Anatomically correct proportions
        - Hyper-detailed:
            * Skin: Visible pores, natural imperfections
            * Hair: Individual strands, texture-appropriate
            * Fabric: Material-accurate (denim/knit/silk etc.)
        3. Prohibited:
        - Stylized interpretations
        - Asymmetry/distortions
        - Artificial-looking textures
        - Color bleeding or mismatches
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


# View to list alll characters 
class CharacterListView(LoginRequiredMixin, ListView):
    model = Character
    template_name = "characters/character_list.html"
    context_object_name = "characters"

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)


# View to update a character 
class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_update.html"
    success_url = reverse_lazy("character-list")

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)


# View to delete a character 
class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    model = Character
    template_name = "characters/character_confirm_delete.html"
    success_url = reverse_lazy("character-list")

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)