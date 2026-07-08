from flask import Blueprint, send_file
from flask_login import login_required

import pandas as pd

from models.attendance import Attendance

report_bp = Blueprint("report", __name__)


@report_bp.route("/export/excel")
@login_required
def export_excel():

    data = Attendance.query.all()

    rows = []

    for i in data:

        rows.append({

            "Student": i.student_id,

            "Subject": i.subject,

            "Date": i.date,

            "Status": i.status

        })

    df = pd.DataFrame(rows)

    file = "attendance.xlsx"

    df.to_excel(file,index=False)

    return send_file(file,as_attachment=True)