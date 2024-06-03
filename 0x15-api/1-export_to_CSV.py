#!/usr/bin/python3
"""
A Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def get_user_info(EMPLOYEE_ID):
    """
    Function to get the USER INFO by USER ID
    """
    try:
        """ Fetch all the employee data from the url """
        response = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}'
                )
        response.raise_for_status()
        employee_data = response.json()

        """ Get the name of the employee """
        employee_name = employee_data.get('name')

        """Get the employee user name """
        user_name = employee_data.get('username')

        """ Fet the employee TODO list data """
        todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}'
                )
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        """ Get the number of tasks """
        total_tasks = len(todo_data)
        t = total_tasks

        """ Get the number of completed task/tasks """
        completed_tasks = [task for task in todo_data if task.get('completed')]

        num_of_tasks_done = len(completed_tasks)
        n = num_of_tasks_done

        """ Displaying the results """
        file_name = f"{EMPLOYEE_ID}.csv"
        with open(file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
            for task in todo_data:
                csv_writer.writerow(
                    [EMPLOYEE_ID, user_name, task.get('completed'),
                        task.get('title')]
                    )

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
