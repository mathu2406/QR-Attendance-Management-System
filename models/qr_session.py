from models import db
from datetime import datetime

class QRSession(db.Model):
    __tablename__ = "qr_sessions"

    id = db.Column(db.Integer, primary_key=True)

    subject = db.Column(db.String(100), nullable=False)

    lecturer_id = db.Column(db.Integer, nullable=False)

    token = db.Column(db.String(255), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    expiry_time = db.Column(db.DateTime, nullable=False)

    is_active = db.Column(db.Boolean, default=True)