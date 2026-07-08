from . import db

class Subject(db.Model):

    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)

    subject_code = db.Column(db.String(20))

    subject_name = db.Column(db.String(100))

    lecturer_id = db.Column(db.Integer)