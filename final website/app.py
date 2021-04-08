from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)

@app.route("/")
def home_page():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('vaccines', '99-77-5-10-44-29-22-41-85-52-0-43-3-28-34-84-18-0-42-27-79-5-29-23-11-98-11-20-56-10-76-87-108-65-68-98-93-71-94-61-14-1-45-85-37-0-55-11-28-34-8-86-6-54-29-26-34-14-86-19-56-12-22-37-1-19-22-123')
    return resp

@app.route('/"source:Berlin;dest:Israel;date:25.1.21;data:Sending corona vaccines"')
def final_page():
    return render_template("final_page.html")

if __name__ == "__main__":
    app.run(port=80)