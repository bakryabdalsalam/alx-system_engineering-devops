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
        with open('{}.csv'.format(ID), 'w') as f:
            for todo in todos:
                f.write(
                        '"{}","{}","{}","{}"\n'.format(
                            ID,
                            username,
                            todo.get('completed'),
                            todo.get('title')
                        )
                )
