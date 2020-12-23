from flask import Blueprint, render_template

main = Blueprint("main", __name__) # Instantiating a blue print

@main.route("/") # Routing
def index():
    context = dict()
    context["num1"] = 23
    context["num2"] = 1997

    return render_template("index.html") # Rendering what to be seen on the template


@main.route("/sign")
def sign():
   
    return render_template("sign.html")

