from flask import Flask, request, jsonify

app = Flask(__name__)

# dummy data for demonstration purposes (replace with your actual database)
colleges_data = {
    "Sri Chaitanya": {
        "Telangana": {
            "Hyderabad": {
                "KPHB": {
                    "Section A": [
                        {"id": 1, "name": "John", "section": "A", "marks": {"Math": 90, "Science": 85}},
                        {"id": 2, "name": "Alice", "section": "A", "marks": {"Math": 85, "Science": 80}}
                    ],
                    "Section B": [
                        {"id": 3, "name": "Bob", "section": "B", "marks": {"Math": 95, "Science": 90}}
                    ]
                }
            }
        }
    }
}

# role-based permissions
roles_permissions = {
    "Super Admin": ["READ", "WRITE", "UPDATE", "DELETE"],
    "Admin": ["READ", "WRITE"],
    "Teacher": ["READ"],
    "Student": ["READ"]
}

# dummy authentication (replace with your actual authentication mechanism)
def authenticate(username, password):
    return True

# function to check if the user has permission for the operation
def check_permission(role, operation):
    if role in roles_permissions:
        return operation in roles_permissions[role]
    return False

# WRITE data API endpoint
@app.route('/write', methods=['POST'])
def write_data():
    college_name = request.json.get('college')
    section = request.json.get('section')
    role = request.json.get('role')
    data = request.json.get('data')

    if check_permission(role, "WRITE"):
        if college_name in colleges_data and section in colleges_data[college_name]:
            colleges_data[college_name][section].append(data)
            return "Data written successfully", 200
        else:
            return "College or section not found", 404
    else:
        return "You do not have permission to write data", 403

# UPDATE data API endpoint
@app.route('/update', methods=['PUT'])
def update_data():
    college_name = request.json.get('college')
    section = request.json.get('section')
    role = request.json.get('role')
    data_id = request.json.get('id')
    updated_data = request.json.get('data')

    if check_permission(role, "UPDATE"):
        if college_name in colleges_data and section in colleges_data[college_name]:
            for student in colleges_data[college_name][section]:
                if student["id"] == data_id:
                    student.update(updated_data)
                    return "Data updated successfully", 200
            return "Student not found", 404
        else:
            return "College or section not found", 404
    else:
        return "You do not have permission to update data", 403

# DELETE data API endpoint
@app.route('/delete', methods=['DELETE'])
def delete_data():
    college_name = request.json.get('college')
    section = request.json.get('section')
    role = request.json.get('role')
    data_id = request.json.get('id')

    if check_permission(role, "DELETE"):
        if college_name in colleges_data and section in colleges_data[college_name]:
            for i, student in enumerate(colleges_data[college_name][section]):
                if student["id"] == data_id:
                    del colleges_data[college_name][section][i]
                    return "Data deleted successfully", 200
            return "Student not found", 404
        else:
            return "College or section not found", 404
    else:
        return "You do not have permission to delete data", 403

if __name__ == '__main__':
    app.run(debug=True)
