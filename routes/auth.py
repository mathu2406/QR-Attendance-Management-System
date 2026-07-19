from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user

from models import db
from models.user import User

from werkzeug.security import generate_password_hash



auth_bp = Blueprint(
    "auth",
    __name__
)








@auth_bp.route("/forgot-password", methods=["GET","POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]
        new_password = request.form["password"]
        confirm_password = request.form["confirm_password"]


        user = User.query.filter_by(
            email=email
        ).first()


        if not user:

            flash(
                "Email address not found!",
                "danger"
            )

            return redirect(
                url_for("auth.forgot_password")
            )


        if new_password != confirm_password:

            flash(
                "Passwords do not match!",
                "danger"
            )

            return redirect(
                url_for("auth.forgot_password")
            )


        user.password = generate_password_hash(
            new_password
        )


        db.session.commit()


        flash(
            "Password updated successfully. Login now.",
            "success"
        )


        return redirect(
            url_for("auth.login")
        )


    return render_template(
        "auth/forgot_password.html"
    )


# ==========================
# SIGNUP
# ==========================

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")


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

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":


        email = request.form.get("email")

        password = request.form.get("password")

        role = request.form.get("role")



        user = User.query.filter_by(
            email=email,
            role=role
        ).first()



        if user and user.check_password(password):


            login_user(user)


            flash("Login successful")


            # Role based redirect

            if user.role == "admin":

                return redirect(
                    url_for("admin_dashboard")
                )


            elif user.role == "lecturer":

                return redirect(
                    url_for("lecturer_dashboard")
                )


            elif user.role == "student":

                return redirect(
                    url_for("student_dashboard")
                )


            else:

                flash("Invalid user role")

                return redirect(
                    url_for("auth.login")
                )



        else:

            flash(
                "Invalid email, password or role"
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

    flash("Logged out successfully")

    return redirect(
        url_for("auth.login")
    )