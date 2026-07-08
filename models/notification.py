from models import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    lecturer_id = db.Column(db.Integer, nullable=False)

    student_name = db.Column(db.String(100), nullable=False)

    subject = db.Column(db.String(100), nullable=False)

    message = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    is_read = db.Column(db.Boolean, default=False)