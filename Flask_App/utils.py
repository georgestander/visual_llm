import os
import textwrap
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_ideas(prompt):
    # Create a conversation with the system message to set the assistant's role
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    
    # Call the OpenAI API to generate a completion based on the prompt
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    # Extract the generated ideas from the response
    # Use the 'message' attribute to access the content
    ideas_text = completion.choices[0].message.content  # Note the change here from ["content"] to .content
    
    # Wrap the text at 60 characters for display purposes
    ideas = textwrap.wrap(ideas_text, 60)
    
    return ideas
