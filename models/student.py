from . import db

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    registration_no = db.Column(db.String(20), unique=True)

    first_name = db.Column(db.String(50))

    last_name = db.Column(db.String(50))

    email = db.Column(db.String(100), unique=True)

    phone = db.Column(db.String(20))

    department = db.Column(db.String(100))

    course = db.Column(db.String(100))

    year = db.Column(db.Integer)

    password = db.Column(db.String(255))

    attendance_percentage = db.Column(db.Float, default=0)

    eligible = db.Column(db.Boolean, default=False)