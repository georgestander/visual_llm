import pathlib
import textwrap
import os

import google.generativeai as genai

import os

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)



def generate_ideas(prompt):
  response = genai.generate_text(prompt, max_output_tokens=300)
  ideas = textwrap.wrap(response.result, 60)
  return ideas
