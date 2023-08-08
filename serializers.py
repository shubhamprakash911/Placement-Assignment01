def validate_employee_data(data):
    required_fields = ['name', 'designation', 'salary']
    for field in required_fields:
        if field not in data:
            return False
    return True

def validate_company_data(data):
    required_fields = ['company_name', 'location', 'founded_year']
    for field in required_fields:
        if field not in data:
            return False
    return True

def read_excel_data(file_path):
    return pd.read_excel(file_path)

def serialize_employee_data(data):
    serialized_data = []
    for index, row in data.iterrows():
        if validate_employee_data(row):
            serialized_data.append({
                'name': row['name'],
                'designation': row['designation'],
                'salary': row['salary']
            })
    return serialized_data

def serialize_company_data(data):
    serialized_data = []
    for index, row in data.iterrows():
        if validate_company_data(row):
            serialized_data.append({
                'company_name': row['company_name'],
                'location': row['location'],
                'founded_year': row['founded_year']
            })
    return serialized_data

