from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .salary_utils import fetch_employees, post_salary_update
from .employee_module import Employee

@csrf_exempt
def employee_api(request):
    if request.method == 'GET':
        # Return employee data as JSON
        file_path = os.path.join(os.path.dirname(__file__), 'employees.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
        return JsonResponse(data)
    
    elif request.method == 'POST':
        # Update employee salary (simulated)
        try:
            data = json.loads(request.body)
            return JsonResponse({"status": "success", "message": "Salary updated"})
        except:
            return JsonResponse({"status": "error", "message": "Invalid data"})
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

def employee_list(request):
    # Display employee list
    file_path = os.path.join(os.path.dirname(__file__), 'employees.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return render(request, 'employees/employee_list.html', {
        'employees': data['employees']
    })

def apply_bonus_view(request):
    # Get bonus percentage from request or default to 10
    bonus_percentage = request.GET.get('bonus_percentage', 10)
    try:
        bonus_percentage = float(bonus_percentage)
    except:
        bonus_percentage = 10
    
    employees = fetch_employees()
    updated_employees = []
    
    for employee in employees:
        final_salary = employee.apply_bonus(bonus_percentage)
        post_salary_update(employee)
        updated_employees.append({
            'emp_id': employee.emp_id,
            'name': employee.name,
            'salary': employee.salary,
            'bonus': round(employee.bonus, 2),
            'final_salary': round(final_salary, 2)
        })
    
    return render(request, 'employees/apply_bonus.html', {
        'employees': updated_employees,
        'bonus_percentage': bonus_percentage
    })

def report_view(request):
    # Get bonus percentage from request or default to 10
    bonus_percentage = request.GET.get('bonus_percentage', 10)
    try:
        bonus_percentage = float(bonus_percentage)
    except:
        bonus_percentage = 10
    
    employees = fetch_employees()
    updated_employees = []
    total_original_salary = 0
    total_bonus = 0
    total_final_salary = 0
    
    for employee in employees:
        final_salary = employee.apply_bonus(bonus_percentage)
        updated_employees.append({
            'emp_id': employee.emp_id,
            'name': employee.name,
            'salary': employee.salary,
            'bonus': round(employee.bonus, 2),
            'final_salary': round(final_salary, 2)
        })
        total_original_salary += employee.salary
        total_bonus += employee.bonus
        total_final_salary += final_salary
    
    return render(request, 'employees/report.html', {
        'employees': updated_employees,
        'bonus_percentage': bonus_percentage,
        'total_original_salary': round(total_original_salary, 2),
        'total_bonus': round(total_bonus, 2),
        'total_final_salary': round(total_final_salary, 2)
    })