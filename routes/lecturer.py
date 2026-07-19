from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import qrcode
import uuid
import os
from datetime import datetime

lecturer_bp = Blueprint(
    "lecturer",
    __name__,
    url_prefix="/lecturer"
)



@lecturer_bp.route("/generate-qr", methods=["GET","POST"])
@login_required
def generate_qr():

    qr_image = None


    if request.method == "POST":


        subject = request.form.get("subject")


        if subject:


            # Unique QR Token

            token = str(uuid.uuid4())



            # QR Data

            qr_data = (
                f"Attendance System\n"
                f"Subject: {subject}\n"
                f"Token:{token}"
            )



            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )


            qr.add_data(qr_data)

            qr.make(
                fit=True
            )


            img = qr.make_image(
                fill_color="black",
                back_color="white"
            )



            # Save folder

            folder = "static/qr"


            os.makedirs(
                folder,
                exist_ok=True
            )


            filename = f"{token}.png"



            filepath = os.path.join(
                folder,
                filename
            )


            img.save(filepath)



            qr_image = "/" + filepath



    return render_template(
        "lecturer/generate_qr.html",
        qr_image=qr_image
    )


@lecturer_bp.route("/lecturer/session")
@login_required
def live_session():

    if current_user.role != "lecturer":
        return "Access Denied"

    return render_template("lecturer/session.html")

