from flask import Blueprint, render_template

main = Blueprint("main", __name__) # Instantiating a blue print

@main.route("/") # Routing
def index():

    return "<h1>Hello Flask. This is me Shedrack Godson</h1>" # Rendering what to be seen on the template

