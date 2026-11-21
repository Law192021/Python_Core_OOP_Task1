
import csv
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
with open("employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    employees = list(reader)
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)
high_earners = [
    emp for emp in employees
    if int(emp["salary"]) > 50000
]
with open("high_earners.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=employees[0].keys()
    )
    writer.writeheader()
    writer.writerows(high_earners)
print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()
    users = response.json()
    for user in users[:3]:
        print(
            f'{user.get("id")} - '
            f'{user.get("name")} - '
            f'{user.get("email")}'
        )
    user_details = []
    for user in users:
        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "company": user.get("company", {}).get("name")
        })
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(user_details, file, indent=4)
except requests.exceptions.Timeout:
    print("Error: Request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Connection failed")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.RequestException as e:
    print("Request Error:", e)
try:
    error_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )
    if error_response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        error_response.raise_for_status()
except requests.exceptions.Timeout:
    print("Error: Request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Connection failed")
except requests.exceptions.RequestException as e:
    print("Request Error:", e)
