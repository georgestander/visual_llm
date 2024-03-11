from flask import Flask
from flask import render_template
from flask import request
import utils


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ideas", methods=["POST"])
def ideas():
    prompt = request.form["prompt"]
    ideas = utils.generate_ideas(prompt)
    return render_template("ideas.html", ideas=ideas)
