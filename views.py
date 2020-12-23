from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Comment

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
    
    # Create a comment object
    comment_obj = Comment(
        name = name,
        comment = comment
    )

    # Commiting the db
    db.session.add(comment_obj)
    db.session.commit()
    # Redirecting to the home page
    return redirect(url_for("main.index"))

