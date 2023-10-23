!#/usr/bin/python3
#it it is meant to be it will be
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    
    if 'name' not in user_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = user_data['name']
    
    # Fetch employee's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()
    
    completed_tasks = [task for task in todos_data if task['completed']]
    
    total_tasks = len(todos_data)
    completed_tasks_count = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
