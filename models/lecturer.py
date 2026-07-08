from . import db

class Lecturer(db.Model):

    __tablename__ = "lecturers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100), unique=True)

    department = db.Column(db.String(100))

    password = db.Column(db.String(255))