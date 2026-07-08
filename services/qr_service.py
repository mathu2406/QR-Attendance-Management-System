# import qrcode
# import uuid
# from datetime import datetime, timedelta

# from models import db
# from models.qr_session import QRSession


# def generate_qr(subject, lecturer_id):

#     token = str(uuid.uuid4())

#     expiry = datetime.utcnow() + timedelta(minutes=5)

#     session = QRSession(
#         subject=subject,
#         lecturer_id=lecturer_id,
#         token=token,
#         expiry_time=expiry,
#         is_active=True
#     )

#     db.session.add(session)
#     db.session.commit()

#     # qr_data = f"http://127.0.0.1:5000/scan/{token}"
#     qr_data = f"http://10.167.158.177:5000/scan/{token}"

#     img = qrcode.make(qr_data)

#     path = f"static/qr/{token}.png"
#     img.save(path)

#     return path, token

import uuid
import qrcode
import os
from datetime import datetime, timedelta

from models import db
from models.qr_session import QRSession


def generate_qr(subject, lecturer_id):

    token = str(uuid.uuid4())

    expiry = datetime.utcnow() + timedelta(minutes=5)

    qr = QRSession(
        subject=subject,
        lecturer_id=lecturer_id,
        token=token,
        expiry_time=expiry,
        is_active=True
    )

    db.session.add(qr)
    db.session.commit()

    qr_data = f"http://10.167.158.177:5000/scan/{token}"
    qr_url = f"http://127.0.0.1:5000/scan/{token}"

    folder = "static/qr"
    os.makedirs(folder, exist_ok=True)

    filename = f"{token}.png"
    filepath = os.path.join(folder, filename)

    img = qrcode.make(qr_url)
    img.save(filepath)

    return filename, token