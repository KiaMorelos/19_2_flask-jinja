from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "its_a_secret_to_everybody"
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    word_list = story.prompts
    return render_template("form.html", words=word_list)

@app.route('/story')
def story_view():
    madlib = story.generate(request.args)
    return render_template("story.html", madlib=madlib)

