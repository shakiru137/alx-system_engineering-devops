#!/usr/bin/python3
"""
A Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def get_user_info(EMPLOYEE_ID):
    """
    Function to get the USER INFO by USER ID
    """
    try:
        """ Fetch all the employee data from the url """
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}')
        response.raise_for_status()
        employee_data = response.json()

        """ Get the name of the employee """
        employee_name = employee_data.get('name')

        """ Fet the employee TODO list data """
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}')
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        """ Get the number of tasks """
        total_tasks = len(todo_data)

        """ Get the number of completed task/tasks """
        completed_tasks = [task for task in todo_data if task.get('completed')]

        num_of_done_tasks = len(completed_tasks)

        """ Displaying the results """
        print(f"Employee {employee_name} is done with tasks ({num_of_done_tasks}/{total_tasks}):")

        """ Displaying title of each task """
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            if employee_id <= 0:
                raise ValueError("Employee ID must be a positive integer")
            get_user_info(employee_id)
        except ValueError:
            print("Please enter a valid integer for employee ID")
