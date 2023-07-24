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
    if len(sys.argv) > 1:
        ID = sys.argv[1]
        user_res = requests.get(
                API_URL + '/users/' + ID + '/todos'
        )
        todos_res = requests.get(
            API_URL + '/users/' + ID
        ).text
        todos = json.loads(user_res.text)
        done = []
        numberOfTasks = 0
        numberOfDone = 0
        employee = json.loads(todos_res)
        nameOfEmployee = employee.get('name')
        for todo in todos:
            numberOfTasks += 1
            if todo.get('completed') is True:
                numberOfDone += 1
                done.append(todo.get('title'))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                nameOfEmployee,
                numberOfDone,
                numberOfTasks
            )
        )
        [print('\t ' + i) for i in done]
