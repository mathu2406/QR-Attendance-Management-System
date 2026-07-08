from flask import Blueprint, redirect
from flask_login import login_required, current_user
from datetime import datetime

from models import db
from models.user import User
from models.attendance import Attendance
from models.qr_session import QRSession
from models.notification import Notification

qr_bp = Blueprint("qr", __name__)


@qr_bp.route("/scan/<token>")
@login_required
def scan(token):

    if current_user.role != "student":
        return "Only students can scan"

    qr = QRSession.query.filter_by(
        token=token,
        is_active=True
    ).first()

    if not qr:
        return "Invalid QR"

    if qr.expiry_time < datetime.utcnow():
        return "QR Expired"

    today = datetime.utcnow().date()

    existing = Attendance.query.filter_by(
        student_id=current_user.id,
        subject=qr.subject,
        date=today
    ).first()

    if existing:
        return "Attendance already marked"

    # Save attendance
    attendance = Attendance(
        student_id=current_user.id,
        subject=qr.subject
    )

    db.session.add(attendance)

    # Update attendance percentage
    current_user.present_classes += 1
    current_user.total_classes += 1

    current_user.attendance = round(
        (current_user.present_classes / current_user.total_classes) * 100,
        2
    )

    # Save notification
    notification = Notification(
        lecturer_id=qr.lecturer_id,
        student_name=current_user.name,
        subject=qr.subject,
        message=f"{current_user.name} marked attendance for {qr.subject}"
    )

    db.session.add(notification)

    db.session.commit()

    return redirect("/student/dashboard")