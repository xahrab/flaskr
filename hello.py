from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Zahra"
    return render_template("index.html", first_name = first_name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#create custom errors pages

#invalid url 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500