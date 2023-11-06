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

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = len([todo for todo in todos_data if todo['completed']])

    return employee_name, completed_tasks, total_tasks, todos_data

def print_todo_progress(employee_name, completed_tasks, total_tasks, todos_data):
    print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')
    for todo in todos_data:
        if todo['completed']:
            print(f'    {todo["title"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks, total_tasks, todos_data = get_employee_info(employee_id)
    print_todo_progress(employee_name, completed_tasks, total_tasks, todos_data)
