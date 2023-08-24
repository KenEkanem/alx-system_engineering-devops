#!/usr/bin/python3
""" Gather data from an API """

import json
import requests
import sys


def to_json(u_id):
    url = 'https://jsonplaceholder.typicode.com/'

    try:
        users = requests.get('{}users'.format(url)).json()
        todos = requests.get('{}todos'.format(url)).json()
    except Exception as e:
        print('Not successful')
        quit()

    task_list = []

    for user in users:
        if user.get('id') == int(u_id):
            for todo in todos:
                if todo.get('userId') == int(u_id):
                    task = {"task": todo.get('title'),
                            "completed": todo.get('completed'),
                            "username": user.get('username')}
                    task_list.append(task)
            user_dict = {user.get('id'): task_list}
            break

    _file = '{}.json'.format(u_id)
    with open(_file, 'w', encoding='utf-8') as f:
        json.dump(user_dict, f)
    f.close()


if __name__ == "__main__":
    to_json(sys.argv[1])
