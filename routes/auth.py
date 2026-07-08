from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user

from models import db
from models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


# ==========================
# SIGNUP
# ==========================

@auth_bp.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        role = request.form["role"]


        existing_user = User.query.filter_by(
            email=email
        ).first()


        if existing_user:

            flash("Email already registered")

            return redirect(
                url_for("auth.signup")
            )


        user = User(

            name=name,

            email=email,

            role=role

        )


        user.set_password(password)


        db.session.add(user)

        db.session.commit()


        flash("Registration successful")

        return redirect(
            url_for("auth.login")
        )


    return render_template(
        "auth/signup.html"
    )



# ==========================
# LOGIN
# ==========================

@auth_bp.route("/login", methods=["GET","POST"])
def login():


    if request.method == "POST":


        email = request.form["email"]

        password = request.form["password"]

        role = request.form["role"]



        user = User.query.filter_by(
            email=email,
            role=role
        ).first()



        if user and user.check_password(password):


            login_user(user)



            if user.role == "admin":

                return redirect(
                    "/admin/dashboard"
                )


            elif user.role == "lecturer":

                return redirect(
                    "/lecturer/dashboard"
                )


            elif user.role == "student":

                return redirect(
                    "/student/dashboard"
                )



        else:

            flash(
                "Invalid login details"
            )



    return render_template(
        "auth/login.html"
    )



# ==========================
# LOGOUT
# ==========================

@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )