# api.py
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
from models import Employee, Company
from serializers import serialize_employee_data, serialize_company_data

api_bp = Blueprint('api', __name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        employee_file = request.files.get('employee_file')
        company_file = request.files.get('company_file')

        if not employee_file or not company_file:
            return jsonify({"error": "Both employee and company files are required."}), 400

        employee_filename = secure_filename(employee_file.filename)
        company_filename = secure_filename(company_file.filename)

        employee_file.save(os.path.join(app.config['UPLOAD_FOLDER'], employee_filename))
        company_file.save(os.path.join(app.config['UPLOAD_FOLDER'], company_filename))

        employee_data = serialize_employee_data(read_excel_data(os.path.join(app.config['UPLOAD_FOLDER'], employee_filename)))
        company_data = serialize_company_data(read_excel_data(os.path.join(app.config['UPLOAD_FOLDER'], company_filename)))

        if not employee_data or not company_data:
            return jsonify({"error": "Invalid data in the uploaded files."}), 400

        # Perform bulk insert and commit here

        return jsonify({"message": "Data uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500
