from flask import Flask, render_template, request, session
from utils import generate_ideas, get_assistant_response
import os
from socket import SOL_SOCKET, SO_REUSEADDR
from werkzeug.serving import make_server

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    chat_history = session.get('chat_history', [])
    ideas = session.get('ideas', [])

    if request.method == 'POST':
        prompt = request.form['prompt']
        chat_history.append({'role': 'user', 'content': prompt})

        # Get the assistant's response
        assistant_response = get_assistant_response(prompt)

        # Append the assistant's response to the chat history
        chat_history.append({'role': 'assistant', 'content': assistant_response})

        # Generate ideas
        ideas = generate_ideas(assistant_response)

        # Save the chat history and the ideas in the session
        session['chat_history'] = chat_history
        session['ideas'] = ideas

    return render_template('index.html', chat_history=chat_history, ideas=ideas)

class CustomServer:
    def __init__(self, host, port, app, **options):
        self.server = make_server(host, port, app, **options)
        self.server.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

def run_custom_server(app, host='127.0.0.1', port=5001):
    from werkzeug.serving import run_simple
    run_simple(hostname=host, port=port, application=app, use_reloader=True, use_debugger=True, threaded=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
