# from flask import Blueprint, render_template
# from flask_login import login_required, current_user

# student_bp = Blueprint("student", __name__)

# @student_bp.route("/student/dashboard")
# @login_required
# def dashboard():
#     if current_user.role != "student":
#         return "Access Denied"

#     return render_template("student/dashboard.html", user=current_user)


# @student_bp.route("/student/profile")
# @login_required
# def profile():
#     if current_user.role != "student":
#         return "Access Denied"
    
#     if not current_user.is_authenticated:
#         return redirect("/login")

#     return render_template("student/profile.html", user=current_user)

# @student_bp.route("/student/scan")
# @login_required
# def scan_page():

#     if current_user.role != "student":
#         return "Access Denied"

#     return render_template("student/scan.html")

# from flask import Blueprint, render_template, redirect
# from flask_login import login_required, current_user

# student_bp = Blueprint("student", __name__)


# @student_bp.route("/student/dashboard")
# @login_required
# def dashboard():

#     if current_user.role != "student":
#         return "Access Denied"

#     return render_template("student/dashboard.html", user=current_user)


# @student_bp.route("/student/profile")
# @login_required
# def profile():

#     if current_user.role != "student":
#         return "Access Denied"

#     return render_template("student/profile.html", user=current_user)


# @student_bp.route("/student/scan")
# @login_required
# def scan_page():

#     if current_user.role != "student":
#         return "Access Denied"

#     return render_template("student/scan.html")

# 


from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.attendance import Attendance


student_bp = Blueprint("student", __name__)


@student_bp.route("/student/dashboard")
@login_required
def dashboard():

    if current_user.role != "student":
        return "Access Denied"


    records = Attendance.query.filter_by(
        student_id=current_user.id
    ).order_by(
        Attendance.date.desc()
    ).all()


    return render_template(
        "student/dashboard.html",
        user=current_user,
        records=records
    )



@student_bp.route("/student/scan")
@login_required
def scan_page():

    if current_user.role != "student":
        return "Access Denied"


    return render_template(
        "student/scan.html"
    )