from datetime import datetime

from models import db


class Attendance(db.Model):

    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer)

    lecturer_id = db.Column(db.Integer)

    date = db.Column(db.Date, default=datetime.utcnow)

    time = db.Column(db.Time, default=datetime.utcnow)

    status = db.Column(db.String(20), default="Present")