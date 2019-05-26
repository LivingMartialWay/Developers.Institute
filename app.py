from flask import Flask
from flask import render_template
app = Flask(__name__)

from profiles import profiles, find_profile
from statuses import statuses, get_status


@app.route("/")
def index():
    return render_template('index.html', x=profiles)


@app.route("/profiles/<username>")
def profile(username):
    profile = find_profile(username)
    statuses = get_status(username)

    return render_template('profile.html', profile=profile , statuses=statuses )

@app.route("/profiles/<username>/friend'id' % usernames")
def friends(username):
    pass
