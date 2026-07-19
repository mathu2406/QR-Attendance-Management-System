from flask_login import UserMixin
from models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))

    # ✅ ADD THESE 2 LINES
    total_classes = db.Column(db.Integer, default=0)
    present_classes = db.Column(db.Integer, default=0)

    attendance = db.Column(db.Float, default=0)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)