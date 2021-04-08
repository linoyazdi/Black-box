import flask
import os
import sqlite3



###### App configuration
app = flask.Flask(__name__)
app.config.from_object(__name__)
app.database = 'sample.db'



##### configure app urls
from routes import (
main
)

def get_about():
    if flask.request.method == "GET":
        return flask.render_template("about.html")
    flask.flash("method not allowed")
    return flask.redirect(flask.url_for("about"))

app.add_url_rule("/", "index", main.handle_request)
app.add_url_rule("/about.html", "about", get_about)