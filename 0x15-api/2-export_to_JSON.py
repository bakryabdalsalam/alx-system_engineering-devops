#!/usr/bin/python3
'''
    Using the https://jsonplaceholder.typicode.com/guide/ API, for a given
    employee ID, returns information about his/her TODO list progress.
'''
import json
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL'''


if __name__ == "__main__":
    '''
        Execute only if run as script.
    '''
    if len(sys.argv) > 1:
        ID = sys.argv[1]
        user_res = requests.get(
                API_URL + '/users/' + ID + '/todos'
        )
        todos_res = requests.get(
            API_URL + '/users/' + ID
        ).text
        todos = json.loads(user_res.text)
        employee = json.loads(todos_res)
        username = employee.get('username')
        with open('{}.json'.format(ID), 'w') as f:
            user_data = list(map(
                lambda x: {
                    'task': x.get('title'),
                    'completed': x.get('completed'),
                    'username': username
                },
                todos
            ))
            users_data = {
                    '{}'.format(ID): user_data
            }
            json.dump(users_data, f)
