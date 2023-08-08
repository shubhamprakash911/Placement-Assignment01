def serialize_employee_data(data):
    serialized_data = []
    for _, row in data.iterrows():
        serialized_data.append({
            'name': row['Name'],
            'designation': row['Designation'],
            'salary': float(row['Salary'])
        })
    return serialized_data

def serialize_company_data(data):
    serialized_data = []
    for _, row in data.iterrows():
        serialized_data.append({
            'company_name': row['Company Name'],
            'location': row['Location'],
            'founded_year': int(row['Founded Year'])
        })
    return serialized_data
