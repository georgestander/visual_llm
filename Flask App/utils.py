import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from google.colab import userdata

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def generate_ideas(prompt):
  response = genai.generate_text(prompt, max_output_tokens=300)
  ideas = textwrap.wrap(response.result, 60)
  return ideas
