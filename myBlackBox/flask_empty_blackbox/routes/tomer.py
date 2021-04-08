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
        username = flask.request.form['uname']
        password = flask.request.form['psw']
        
        with sqlite3.connect(app.database) as connection:
            c = connection.cursor()
            c.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" % (username, password))
            if c.fetchone():
                if (username == "admin"):
                    return flask.render_template('usersData.html')
                elif (username == "bahman" and password == "Terrorist123"):
                    return flask.send_from_directory("files", "my_suitcase.zip", as_attachment=True)
                else:
                    return flask.render_template('notRightUser.html')
            
            else:
                return flask.render_template('failure.html')
