#!/usr/bin/python3
'''
    Using the https://jsonplaceholder.typicode.com/guide/ API, for a given
    employee ID, returns information about his/her TODO list progress.
'''
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL'''


if __name__ == "__main__":
    '''
        Execute only if run as script.
    '''
    users_res = requests.get(API_URL + '/users/')
    todos_res = requests.get(API_URL + '/todos/')
    users_data = {}
    for user in json.loads(users_res.text):
        ID = user.get('id')
        username = user.get('username')
        todos = list(filter(
            lambda x: x.get('userId') == ID, json.loads(todos_res.text)
        ))
        user_data = list(map(
            lambda x: {
                'username': username,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(ID)] = user_data
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_data, f)
