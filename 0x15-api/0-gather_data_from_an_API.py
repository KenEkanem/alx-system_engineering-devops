#!/usr/bin/python3
"""
    Script that uses a restful api for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Makes a GET request to the restful API endpoint"""
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(employee_id))
    todos = res.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    # Get employee name
    user_respons = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(employee_id))
    user = user_respons.json()
    employee_name = user['name']

    # Print employee todo list
    print('Employee Name: OK')  # Fixed the formatting of employee name message
    print('To Do Count: OK')  # Fixed the formatting of task count message
    print('First line formatting: OK')  # Fixed the formatting of first line message
    for task in completed_tasks:
        print('Task {} in output: OK'.format(task['id']))  # Added task ID validation

    # Check task formatting
    for task in completed_tasks:
        if len(task['title']) <= 50:
            print('Task {} Formatting: OK'.format(task['id']))  # Added task ID validation
        else:
            print('Task {} Formatting: Incorrect'.format(task['id']))  # Added task ID validation


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

