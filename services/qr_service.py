import qrcode
import uuid
from datetime import datetime, timedelta

from models import db
from models.qr_session import QRSession


def generate_qr(subject, lecturer_id):

    token = str(uuid.uuid4())

    expiry = datetime.utcnow() + timedelta(minutes=5)

    session = QRSession(
        subject=subject,
        lecturer_id=lecturer_id,
        token=token,
        expiry_time=expiry,
        is_active=True
    )

    db.session.add(session)
    db.session.commit()

    qr_data = f"http://127.0.0.1:5000/scan/{token}"

    img = qrcode.make(qr_data)

    path = f"static/qr/{token}.png"
    img.save(path)

    return path, token