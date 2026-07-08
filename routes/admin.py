from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from reportlab.pdfgen import canvas

from models.user import User
from models.attendance import Attendance
from models.qr_session import QRSession

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin/dashboard")
@login_required
def dashboard():

    if current_user.role != "admin":
        return redirect("/login")

    total_students = User.query.filter_by(role="student").count()
    total_lecturers = User.query.filter_by(role="lecturer").count()

    total_attendance = Attendance.query.count()

    total_qr = QRSession.query.count()

    return render_template(
        "admin/dashboard.html",
        students=total_students,
        lecturers=total_lecturers,
        attendance=total_attendance,
        qr=total_qr
    )


@admin_bp.route("/admin/students")
@login_required
def students():

    users = User.query.filter_by(role="student").all()

    return render_template(
        "admin/students.html",
        users=users
    )


@admin_bp.route("/admin/lecturers")
@login_required
def lecturers():

    users = User.query.filter_by(role="lecturer").all()

    return render_template(
        "admin/lecturers.html",
        users=users
    )


@admin_bp.route("/admin/attendance")
@login_required
def attendance():

    records = Attendance.query.all()

    return render_template(
        "admin/attendance.html",
        records=records
    )


@admin_bp.route("/admin/export/pdf")
@login_required
def export_pdf():

    if current_user.role != "admin":
        return redirect("/login")

    pdf = "attendance_report.pdf"

    c = canvas.Canvas(pdf)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 820, "Attendance Management System")

    c.setFont("Helvetica", 12)
    c.drawString(220, 800, "Attendance Report")

    y = 760

    records = Attendance.query.all()

    for r in records:

        c.drawString(
            40,
            y,
            f"Student ID: {r.student_id} | Subject: {r.subject} | Date: {r.date} | Status: {r.status}"
        )

        y -= 20

        # Create a new page if needed
        if y < 50:
            c.showPage()
            y = 800

    c.save()

    return send_file(pdf, as_attachment=True)