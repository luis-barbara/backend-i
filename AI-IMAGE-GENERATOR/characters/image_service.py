import openai
from django.conf import settings
import logging



logger = logging.getLogger(__name__)

openai.api_key = settings.OPENAI_API_KEY 

def generate_image(prompt: str):
    """Call the OpenAI API to generate an image based on the prompt."""
    try:
        # Call the DALL·E API to generate an image
        response = openai.Image.create(
            model="dall-e-3",  
            prompt=prompt,     
            size="1024x1024", 
            n=1                
        )
        
        # Extract and return the URL of the generated image
        return response["data"][0]["url"]
    
    except openai.error.OpenAIError as e:
        # Catch OpenAI specific errors
        logger.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        # Catch all other exceptions
        logger.error(f"Error generating image: {e}")
        return None

