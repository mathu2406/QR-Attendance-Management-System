from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user

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


from routes.lecturer import lecturer_bp

app.register_blueprint(
    lecturer_bp
)


# =========================
# Dashboard Redirect
# =========================

@app.route("/dashboard")
@login_required
def dashboard():

    if current_user.role == "student":

        return redirect(
            url_for("student_dashboard")
        )


    elif current_user.role == "lecturer":

        return redirect(
            url_for("lecturer_dashboard")
        )


    elif current_user.role == "admin":

        return redirect(
            url_for("admin_dashboard")
        )


    else:

        return "Invalid Role"



# =========================
# Student Dashboard
# =========================

@app.route("/student/dashboard")
@login_required
def student_dashboard():

    return render_template(
        "student/dashboard.html",
        user=current_user
    )



# =========================
# Lecturer Dashboard
# =========================

@app.route("/lecturer/dashboard")
@login_required
def lecturer_dashboard():

    return render_template(
        "lecturer/dashboard.html",
        user=current_user
    )



# =========================
# Admin Dashboard
# =========================

@app.route("/admin/dashboard")
@login_required
def admin_dashboard():

    return render_template(
        "admin/dashboard.html",
        user=current_user
    )



from flask_socketio import SocketIO

socketio = SocketIO(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )



# =========================
# Run
# =========================

if __name__ == "__main__":
    app.run(debug=True)