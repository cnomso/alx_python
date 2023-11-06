import csv
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos_data = todos_response.json()

    return employee_name, todos_data

def export_to_csv(employee_id, employee_name, todos_data):
    with open(f'{employee_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, todos_data = get_employee_info(employee_id)
    export_to_csv(employee_id, employee_name, todos_data)
