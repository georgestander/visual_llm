from flask import Flask, render_template, request, session
from utils import generate_ideas
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        ideas = generate_ideas(prompt)

        # Store the chat history in the session
        chat_history = session.get('chat_history', [])
        chat_history.append({'role': 'user', 'content': prompt})
        chat_history.extend([{'role': 'assistant', 'content': idea} for idea in ideas])
        session['chat_history'] = chat_history

        return render_template('index.html', ideas=ideas, chat_history=chat_history)
    return render_template('index.html', chat_history=session.get('chat_history', []))
