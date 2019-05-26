from flask import Flask
from flask import render_template
app = Flask(__name__)

from profiles import profiles, find_profile
from statuses import statuses


@app.route("/")
def index():
    return render_template('index.html', profiles=profiles)


@app.route("/profiles/<username>")
def profile(username):
    pass

@app.route("/profiles/<username>/friends")
def friends(username):
    pass


