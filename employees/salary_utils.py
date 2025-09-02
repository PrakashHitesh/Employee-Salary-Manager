import json
import os
from .employee_module import Employee

def fetch_employees():
    employees = []
    file_path = os.path.join(os.path.dirname(__file__), 'employees.json')
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for emp_data in data.get('employees', []):
                employee = Employee(
                    emp_data['id'],
                    emp_data['name'],
                    emp_data['salary']
                )
                employees.append(employee)
    except FileNotFoundError:
        print("employees.json file not found!")
    
    return employees

def post_salary_update(employee):
    # In a real scenario, this would update a database
    print(f"Updated salary for {employee.name}: {employee.salary + employee.bonus}")
    return True