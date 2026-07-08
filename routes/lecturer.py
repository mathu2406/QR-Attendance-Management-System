# from flask import Blueprint, render_template, request, redirect
# from flask_login import login_required, current_user

# from services.qr_service import generate_qr

# lecturer_bp = Blueprint("lecturer", __name__)


# @lecturer_bp.route("/lecturer/dashboard")
# @login_required
# def dashboard():

#     if current_user.role != "lecturer":
#         return "Access Denied"

#     return render_template("lecturer/dashboard.html")


# @lecturer_bp.route("/lecturer/generate-qr", methods=["GET", "POST"])
# @login_required
# def generate_qr_page():

#     if current_user.role != "lecturer":
#         return "Access Denied"

#     if request.method == "POST":

#         subject = request.form["subject"]

#         path, token = generate_qr(subject, current_user.id)

#         return render_template(
#             "lecturer/show_qr.html",
#             qr_image=path,
#             token=token
#         )

#     return render_template("lecturer/generate_qr.html")

# from flask import Blueprint, render_template, request
# from flask_login import login_required, current_user

# from services.qr_service import generate_qr
# from models.notification import Notification

# lecturer_bp = Blueprint("lecturer", __name__)

# @lecturer_bp.route("/lecturer/notifications")
# @login_required
# def notifications():

#     if current_user.role != "lecturer":
#         return "Access Denied"

#     notifications = Notification.query.filter_by(
#         lecturer_id=current_user.id
#     ).order_by(Notification.created_at.desc()).all()

#     return render_template(
#         "lecturer/notifications.html",
#         notifications=notifications
#     )

# @lecturer_bp.route("/lecturer/dashboard")
# @login_required
# def dashboard():

#     if current_user.role != "lecturer":
#         return "Access Denied"

#     return render_template("lecturer/dashboard.html")


# @lecturer_bp.route("/lecturer/generate", methods=["GET", "POST"])
# @login_required
# def generate():

#     if current_user.role != "lecturer":
#         return "Access Denied"

#     qr_image = None

#     if request.method == "POST":

#         subject = request.form["subject"]

#         filename, token = generate_qr(
#             subject,
#             current_user.id
#         )

#         qr_image = filename

#     return render_template(
#         "lecturer/generate_qr.html",
#         qr_image=qr_image
#     )


from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from services.qr_service import generate_qr
from models.notification import Notification

lecturer_bp = Blueprint("lecturer", __name__)

@lecturer_bp.route("/lecturer/dashboard")
@login_required
def dashboard():

    if current_user.role != "lecturer":
        return "Access Denied"

    return render_template("lecturer/dashboard.html")


@lecturer_bp.route("/lecturer/generate", methods=["GET", "POST"])
@login_required
def generate():

    if current_user.role != "lecturer":
        return "Access Denied"

    qr_image = None

    if request.method == "POST":

        subject = request.form["subject"]

        filename, token = generate_qr(subject, current_user.id)

        qr_image = filename

    return render_template(
        "lecturer/generate_qr.html",
        qr_image=qr_image
    )


@lecturer_bp.route("/lecturer/notifications")
@login_required
def notifications():

    if current_user.role != "lecturer":
        return "Access Denied"

    notifications = Notification.query.filter_by(
        lecturer_id=current_user.id
    ).order_by(Notification.created_at.desc()).all()

    return render_template(
        "lecturer/notifications.html",
        notifications=notifications
    )