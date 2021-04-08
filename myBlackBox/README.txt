How to run and access the website:
------------------------
1. first, run:   pip install Flask
2. from flask_empty_black_box run in the cmd:     flask run
3. Open your browser and open http://127.0.0.1:5000/
4. If you see the website- you are good to go. If you can't see the website (or can see but it looks bad) that means that you have a problem
5. whenever you change your code- you need to reload the website (-> cntl+c in the cmd and 'flask run' again) 



How to change to website:
------------------------
1. the file app.py is the main file. You can add url paths to your website by adding commands:
app.add_url_rule("/<your path>", "<your path>", <function to handle the requests>)

2. In folder routes you can see an example to how the GET request for index.html is being processed. If you wish to add your own path say for "/login_page" add this path in app.py and a file under routes and login_page.html file under "templates" directory:
 
>> import routes.login_page
>> app.add_url_rule("/login_page", "login_page", login_page.handle_request)


3. If you wish to change the design (and please do!) you can do that using the css file udner static directory and by adding new HTML file under templates.

4. For any questions please don't hesitate to ask us and to USE GOOGLE! (google search words: "python flask ___")
