#!/usr/bin/python3
"""Request a user's todo lists"""

from json import load
import requests
from sys import argv

if __name__ == "__main__":

    def make_request(resource, param=None):
        """Retrieve user info from API"""
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        result = requests.get(url)
        result = result.json()
        return result

    user = make_request('users', ('id', argv[1]))
    tasks = make_request('todos', ('userId', argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))
