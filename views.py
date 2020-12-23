from flask import (Blueprint, render_template, request,
    redirect, url_for, flash
    )
from . import db
from .models import Comment

main = Blueprint("main", __name__) # Instantiating a blue print

@main.route("/") # Routing
def index():
    comments_qs = Comment.query.all() # Querying all comment objects
    return render_template("index.html", comments_qs=comments_qs) # Rendering what to be seen on the template


@main.route("/sign/")
def sign():
   
    return render_template("sign.html")


@main.route("/sign/", methods=["POST"])
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


@main.route("/sign_delete/<int:id>/", methods=["GET"])
def sign_delete(id=id):
    sign_obj = Comment.query.get(id)
    
    return render_template("sign_delete.html", sign_obj=sign_obj)


@main.route("/sign_delete_post/<int:id>/", methods=["POST"])
def sign_delete_post(id=id):
    sign_obj = Comment.query.get(id) # Getting Object
    db.session.delete(sign_obj) # Delete Object
    db.session.commit()
    flash("Deleted successfully.", "success")
    return redirect(url_for("main.index"))


@main.route("/sign_edit/<int:id>/", methods=["GET"])
def sign_edit(id=id):
    sign_obj = Comment.query.get(id)

    return render_template("sign_edit.html", sign_obj=sign_obj)


@main.route("/sign_edit_request/<int:id>/", methods=["POST"])
def sign_edit_request(id=id):
    sign_obj = Comment.query.get(id) # Getting Object
    name = request.form.get("name")
    comment = request.form.get("comment")
    sign_obj.name = name
    sign_obj.comment = comment
    db.session.add(sign_obj)
    db.session.commit()
    flash("Updated successfully.", "success")
    return redirect(url_for("main.index"))

