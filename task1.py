import csv
class InvalidSalaryError(Exception):
    pass
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)
    if "cap" in options:
        result = min(result, options["cap"])
    return result
print("Bonus:", bonus(50000, 0.1, 1000, 2000, cap=8000))
class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
        return f"Name: {self.name}, Salary: {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"
try:
    emp = Employee("Arun", -500)
except InvalidSalaryError as e:
    print("Error:", e)
finally:
    print("Transaction finished")
emp1 = Employee("Rahul", 60000)
print("Annual Salary:", emp1.annual_salary())
manager1 = Manager("Priya", 90000, 5)
print(manager1.get_details())
with open("employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    print("CSV Columns:", reader.fieldnames)
    employees = [
        {
            "name": row["name"].strip(),
            "salary": int(row["salary"]),
            "city": row["city"].strip()
        }
        for row in reader
    ]
above_50000 = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]
print("Above 50000:", above_50000)
increased_salary = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)
print("10% Salary Raise:", increased_salary)
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)
chennai_names = list(
    map(lambda emp: emp["name"], chennai_employees)
)
print("Chennai:", chennai_names)
salaries = [emp["salary"] for emp in employees]
for salary in salaries:
    if salary == 0:
        continue
    print("Salary:", salary)
    if salary > 85000:
        print("Salary above 85000 found. Stopping loop.")
        break
