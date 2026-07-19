from flask import Blueprint, redirect, url_for, session
from flask_login import current_user
from datetime import datetime

from models import db
from models.qr_session import QRSession
from models.attendance import Attendance
from models.user import User


qr_bp = Blueprint("qr", __name__)


@qr_bp.route("/scan/<token>")
def scan_qr(token):

    if not current_user.is_authenticated:
        session["pending_qr"] = token
        return redirect(url_for("login"))

    if current_user.role != "student":
        return "Only students allowed"

    session_data = QRSession.query.filter_by(token=token, is_active=True).first()

    if not session_data:
        return "Invalid QR"

    if session_data.expiry_time < datetime.utcnow():
        return "QR Expired"

    today = datetime.utcnow().date()

    existing = Attendance.query.filter_by(
        student_id=current_user.id,
        subject=session_data.subject,
        date=today
    ).first()

    if existing:
        return "Already Marked"

    attendance = Attendance(
        student_id=current_user.id,
        subject=session_data.subject,
        status="Present"
    )


    db.session.add(attendance)

    # UPDATE STUDENT ATTENDANCE %
    user = User.query.get(current_user.id)

    user.attendance = min(user.attendance + 2.5, 100)

    db.session.commit()

    return "Attendance Marked Successfully"
    )

    db.session.commit()

    return redirect("/student/dashboard")