from flask import Flask, render_template, request
from utils import generate_ideas

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        ideas = generate_ideas(prompt)
        return render_template('index.html', ideas=ideas)
    return render_template('index.html')
