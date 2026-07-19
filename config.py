import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = "attendance_secret_key"


    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR,
        "database",
        "attendance.db"
    )


    SQLALCHEMY_TRACK_MODIFICATIONS = False



    # Email Configuration

    MAIL_SERVER = "smtp.gmail.com"

    MAIL_PORT = 587

    MAIL_USE_TLS = True


    MAIL_USERNAME = "mathulaaravinthan@gmail.com"

    MAIL_PASSWORD = "YOUR_APP_PASSWORD"