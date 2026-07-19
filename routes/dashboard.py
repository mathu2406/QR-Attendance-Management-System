from flask import Blueprint, render_template
from flask_login import login_required, current_user


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)



# =====================
# ADMIN DASHBOARD
# =====================

@dashboard_bp.route("/admin/dashboard")
@login_required
def admin_dashboard():

    if current_user.role != "admin":
        return "Access Denied"

    return render_template(
        "admin/dashboard.html"
    )



# =====================
# LECTURER DASHBOARD
# =====================

@dashboard_bp.route("/lecturer/dashboard")
@login_required
def lecturer_dashboard():

    if current_user.role != "lecturer":
        return "Access Denied"


    return render_template(
        "lecturer/dashboard.html"
    )



# =====================
# STUDENT DASHBOARD
# =====================

@dashboard_bp.route("/student/dashboard")
@login_required
def student_dashboard():

    if current_user.role != "student":
        return "Access Denied"


    return render_template(
        "student/dashboard.html"
    )