import flask_login

import flask


def handle_request():
    if flask.request.method == "GET":
        return get()
    flask.flash("method not allowed")
    return flask.redirect(flask.url_for("index"))


def get():
    return flask.render_template("index.html")
