from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    hello = "Greetings my lord, welcome to our treasury!"
    current_year = datetime.datetime.now().year
    projects = ["Boogle", "Fakebook", "SideHustle"]
    return render_template("index.html", hello=hello, current_year=current_year, projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/Boogle")
def boogle():
    return render_template("/Boogle/index.html")

@app.route("/Fakebook")
def fakebook():
    return render_template("/Fakebook/Fakebook.html")

@app.route("/SideHustle")
def sidehustle():
    return render_template("/SideHustle/index.html")

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)