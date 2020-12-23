from flask import Blueprint, render_template, request

main = Blueprint("main", __name__) # Instantiating a blue print

@main.route("/") # Routing
def index():

    return render_template("index.html") # Rendering what to be seen on the template


@main.route("/sign")
def sign():
   
    return render_template("sign.html")


@main.route("/sign", methods=["POST"])
def sign_up():
    name = request.form.get("name")
    comment = request.form.get("comment")
    
    return f'Name: {name} Comment: {comment}'

