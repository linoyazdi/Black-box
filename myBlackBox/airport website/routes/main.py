import flask_login
import sqlite3
import flask
import os
from app import app


"""
This function handles any request
"""
def handle_request():
    if flask.request.method == "GET":
        return get()
    flask.flash("method not allowed")
    return flask.redirect(flask.url_for("index"))


"""
This function handles a get request - redirect to index.html
"""
def get():
    return flask.render_template("index.html")


"""
This function handles a login
if Get method:
    redirect to index.html

if Post method:
    getting the username and password from the request
    connecting to the sql app.database
    checking if the user name and password are in the sql table we created
    redirecting according to the result
"""
@app.route('/login', methods=['GET', 'POST'])
def handle_login() -> str:
    if flask.request.method == 'GET':
        return get()
    
    elif flask.request.method == "POST":
        flight = flask.request.form['flight']
        
        if (flight == "ADP9101"):
            return flask.redirect("https://youtu.be/DcbCPHWf4n0", code=302)
        else:
            return flask.render_template("index.html")

@app.route("/download_files")
def download():
    return flask.send_from_directory("files", "files.zip", as_attachment=True)
