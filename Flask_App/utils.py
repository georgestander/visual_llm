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
    
    # Concatenate all assistant messages into one string without separate lines
    ideas_text = " ".join([choice.message.content for choice in completion.choices])
    
    # Return the ideas text as a single string
    return ideas_text


def get_assistant_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    full_response = response.choices[0].message.content
    
    # Split the response by lines
    lines = full_response.split('\n')
    main_response = []
    ideas = []
    for line in lines:
        line = line.strip().lower()
        if line.lower().startswith(('idea:', 'step:', 'suggestion:', '1.', '1)', 'a)', 'i)', 'ii)', 'iii)')):
            ideas.append(line)
        else:
            main_response.append(line)
    
    # Join the non-idea parts as the main response
    main_response = '\n'.join(main_response)
    
    return main_response, ideas
