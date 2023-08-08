from flask import Flask, request, jsonify
from config import DB_CONFIG
from models import db
from database_utils import bulk_insert_employees, bulk_insert_companies
from serializers import read_excel_data, serialize_employee_data, serialize_company_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['db']}"
db.init_app(app)

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        employee_file = request.files.get('employee_file')
        company_file = request.files.get('company_file')

        employee_data = serialize_employee_data(read_excel_data(employee_file))
        company_data = serialize_company_data(read_excel_data(company_file))

        bulk_insert_employees(employee_data)
        bulk_insert_companies(company_data)

        return jsonify({"message": "Data uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
