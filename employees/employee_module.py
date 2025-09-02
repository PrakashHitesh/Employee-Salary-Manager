class Employee:
    def __init__(self, emp_id, name, salary, bonus=0):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.bonus = bonus
    
    def apply_bonus(self, percentage):
        self.bonus = self.salary * (percentage / 100)
        return self.salary + self.bonus
    
    def __str__(self):
        return f"{self.name} | Final Salary: {self.salary + self.bonus}"