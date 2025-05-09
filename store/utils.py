import openai
from django.conf import settings

# Initialize OpenAI API key
openai.api_key = settings.OPENAI_KEY

def generate_tags_from_description(description):
    """Generate tags for a product based on its description using OpenAI API."""
    prompt = f"Generate relevant tags for this product description: {description}"

    try:
        # OpenAI API request (new completion interface)
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # You can use other models like "gpt-4" if needed
            prompt=prompt,
            max_tokens=50,  # Limit the length of the response
            temperature=0.7,  # Controls the randomness of the response
        )

        # Extract tags from the response
        generated_tags = response['choices'][0]['text'].strip()
        tags = [tag.strip() for tag in generated_tags.split(',')]
        return tags

    except Exception as e:
        print(f"Error generating tags: {e}")
        return []
