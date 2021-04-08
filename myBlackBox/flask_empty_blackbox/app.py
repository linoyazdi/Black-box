import flask
import os
import sqlite3



###### App configuration
app = flask.Flask(__name__)
app.config.from_object(__name__)
app.database = 'sample.db'



##### configure app urls
from routes import (
tomer,
terroristPassword,
)

app.add_url_rule("/", "index", tomer.handle_request)
app.add_url_rule("/712942", "712942", terroristPassword.handle_request)

# delete the existing data
if os.path.exists(app.database):
    os.remove(app.database)
    
# create database if it doesn't exist yet    
with sqlite3.connect(app.database) as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE employees(username TEXT, password TEXT)""")
    c.execute('INSERT INTO employees VALUES("admin", "{}")'.format("supersecretpass"))
    c.execute('INSERT INTO employees VALUES("bahman", "{}")'.format("Terrorist123"))
    c.execute('INSERT INTO employees VALUES("zana", "{}")'.format("iloveiran"))
    connection.commit()
    
print("Application is running\n")

#' OR 1=1 --