from flask import Flask, render_template
# from flask_login import LoginManager
from flask_login import LoginManager, current_user, login_required

from config import Config
from models import db
from models.user import User


app = Flask(__name__)
app.config.from_object(Config)


# =========================
# Database
# =========================

db.init_app(app)


# =========================
# Login Manager
# =========================

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# =========================
# Public Pages
# =========================

@app.route("/")
def home():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/contact")
def contact():
    return render_template("public/contact.html")



# =========================
# Authentication Blueprint
# =========================

from routes.auth import auth_bp

app.register_blueprint(auth_bp)



# =========================
# Test Dashboards
# =========================

# @app.route("/student/dashboard")
# def student_dashboard():
#     return render_template("student/dashboard.html")


# @app.route("/lecturer/dashboard")
# def lecturer_dashboard():
#     return render_template("lecturer/dashboard.html")


# @app.route("/admin/dashboard")
# def admin_dashboard():
#     return render_template("admin/dashboard.html")

@app.route("/student/dashboard")
@login_required
def student_dashboard():

    return render_template(
        "student/dashboard.html",
        user=current_user
    )


@app.route("/lecturer/dashboard")
@login_required
def lecturer_dashboard():

    return render_template(
        "lecturer/dashboard.html",
        user=current_user
    )


@app.route("/admin/dashboard")
@login_required
def admin_dashboard():

    return render_template(
        "admin/dashboard.html",
        user=current_user
    )



# =========================
# Run
# =========================

if __name__ == "__main__":
    app.run(debug=True)