# Employee Salary Manager 🏢💰

A Django web application for managing employee salaries and applying bonuses with a beautiful, responsive interface.

![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Learning Outcomes](#-learning-outcomes)

## ✨ Features

- **Employee Management**: View all employees with their details in a clean table format
- **Bonus Calculation**: Apply percentage-based bonuses to employee salaries
- **Detailed Reports**: Generate comprehensive salary reports with bonus calculations
- **Responsive Design**: Beautiful Bootstrap UI that works on desktop and mobile devices
- **RESTful API**: JSON API endpoints for employee data
- **Modular Code**: Well-organized code following Django best practices


## 🛠 Technology Stack

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)
- **Programming Language**: Python 3.11+
- **API Handling**: Django Views, JSON
- **Virtual Environment**: Python venv

## 🚀 Installation

Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrakashHitesh/Employee-Salary-Manager.git
   cd Employee-Salary-Manager
2. **Create and activate virtual environment**
   
   **On Windows**
   
      python -m venv employees_env
      employees_env\Scripts\activate
    
     **On macOS/Linux**
      python -m venv employees_env
      source employees_env/bin/activate
4. **Install dependencies**
      pip install -r requirements.txt

5. **Run database migrations**
      python manage.py makemigrations
      python manage.py migrate
6. **Start the development serve**
      python manage.py runserver
7. **Access the application**
      Open your browser and go to http://localhost:8000/


# 📖 Usage
**Viewing Employees**

    Navigate to the home page to see the list of all employees

    The table displays employee ID, name, salary, and actions

**Applying Bonuses**

    Use the form at the bottom of the page to apply a bonus percentage to all employees

    Or click "Apply 10% Bonus" next to any individual employee

    The system will calculate: Bonus = Salary × (Percentage / 100)

    View the results on the bonus application page

**Generating Reports**

    After applying bonuses, click "View Detailed Report"

    The report shows:

        Original salaries

        Bonus amounts

        Final salaries

        Total calculations

        Percentage increases

**API Access**

    Access employee data via JSON API at /api/employees/

    Returns employee data in JSON format

    Can be used for integration with other applications

# 📁 Project Structure

<img width="700" height="596" alt="image" src="https://github.com/user-attachments/assets/66830af4-ddf1-419c-a100-0f4b7eabbaaa" />



# Contributing

**We welcome contributions to improve this project! Here's how you can help:**

    Fork the repository

    Create a feature branch: git checkout -b feature/amazing-feature

    Make your changes

    Commit your changes: git commit -m 'Add amazing feature'

    Push to the branch: git push origin feature/amazing-feature

    Open a Pull Request

**Areas for Contribution**

    Add authentication and authorization

    Implement database persistence instead of JSON file

    Add more advanced reporting features

    Create unit tests

    Improve UI/UX design

    Add export functionality (PDF, Excel)

#  License

**This project is licensed under the MIT License - see the LICENSE file for details.
**

# 💡 Learning Outcomes

**This project demonstrates:
**

    Django Fundamentals: Models, Views, Templates, URL routing

    Object-Oriented Programming: Employee class with methods

    API Development: JSON endpoints for data exchange

    Frontend Development: Bootstrap integration, responsive design

    Project Structure: Modular code organization

    Version Control: Git and GitHub usage
