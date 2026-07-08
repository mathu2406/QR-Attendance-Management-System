from datetime import datetime

from models import db


class QRSession(db.Model):

    __tablename__ = "qr_sessions"

    id = db.Column(db.Integer, primary_key=True)

    token = db.Column(db.String(200), unique=True)

    lecturer_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    active = db.Column(db.Boolean, default=True)