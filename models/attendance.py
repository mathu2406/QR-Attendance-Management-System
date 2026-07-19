from models import db
from datetime import datetime

# class Attendance(db.Model):
#     __tablename__ = "attendance"

#     id = db.Column(db.Integer, primary_key=True)

#     student_id = db.Column(db.Integer, nullable=False)

#     subject = db.Column(db.String(100), nullable=False)

#     date = db.Column(db.Date, default=datetime.utcnow)

#     status = db.Column(db.String(20), default="Present")


class Attendance(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(120))

    ati_number = db.Column(db.String(30))

    qr_token = db.Column(db.String(100))