import pytest
from django.urls import reverse
from unittest.mock import patch

# Tests if the homepage (index) loads correctly and uses the correct template.
@pytest.mark.django_db
def test_homepage(client):
    """
    This test checks if the homepage (index) loads correctly.
    It verifies that the response has a status code 200 (OK) and that the 'characters/index.html' template is used.
    """
    url = reverse('index')  
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'characters/index.html' in [t.name for t in response.templates]  


# Tests if an authenticated user can access the character list page.
@pytest.mark.django_db
def test_authenticated_view(client, django_user_model):
    """
    This test simulates a user logging in and accessing the character list view.
    It checks if the response status is 200 (OK) after the user is logged in.
    """
    # Create and login a test user
    user = django_user_model.objects.create_user(username='test', password='test')
    client.force_login(user)
    
    response = client.get(reverse('character-list'))
    assert response.status_code == 200


# Fixture that provides valid character creation data for the tests.
@pytest.fixture
def valid_character_data():
    """
    This fixture provides valid data for creating a new character.
    It returns a dictionary of character attributes like title, age, gender, and other details.
    """
    return {
        'title': 'Test Character',
        'age': 25,
        'gender': 'M',
        'skin': 'LT',
        'ethnicity': 'WH',
        'eye_color': 'BL',
        'hair_color': 'BK',
        'hair_style': 'SH_WG',
        'clothing': 'LB_SJ_DJ',
        'clothing_style': 'CA',
        'accessories': 'WW_SG',
        'expression': 'SM',
        'pose': 'FF_UP',
        'image_style': 'RL',
        'image_texture': 'SM',
        'image_dominant_colors': 'NE',
        'image_contrast': 'MD',
        'image_shading': 'SO',
        'image_lighting': 'SD',
        'image_additional_details': 'NB_UR',
        'camera': 'CANON_XTi',
        'lens': '100_300mm_f5_6',
        'iso': 'ISO_200',
        'exposure': '1_160',
    }

# Tests if a new character can be created and checks if the image generation service is mocked correctly.
@pytest.mark.django_db
@patch('characters.image_service.generate_image')
def test_character_creation(mock_generate, client, django_user_model, valid_character_data):
    """
    This test simulates the creation of a new character by an authenticated user.
    It mocks the image generation service and ensures the character is created successfully.
    The test also checks if the response contains the correct success message and if the new character is saved in the database.
    """
    # Setup mock and user
    mock_generate.return_value = "http://mocked.image.url"
    user = django_user_model.objects.create_user(username='test', password='test')
    client.force_login(user)
    
    # Make the request
    response = client.post(reverse('character-create'), valid_character_data)
    
    # Debug information
    if response.status_code != 200:
        print("Unexpected status code:", response.status_code)
        if hasattr(response, 'context') and 'form' in response.context:
            print("Form errors:", response.context['form'].errors)
    
    # Check the response
    assert response.status_code == 200  
    assert 'form' in response.context  
    assert 'new_character' in response.context  
    
    # Verify the character was actually created
    from characters.models import Character
    assert Character.objects.filter(title=valid_character_data['title']).exists()
    
    # Verify success message
    messages = list(response.context['messages'])
    assert len(messages) == 1
    assert "success" in messages[0].tags
    assert "created successfully" in messages[0].message