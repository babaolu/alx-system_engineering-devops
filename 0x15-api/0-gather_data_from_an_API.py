#!/usr/bin/python3
""" Displays todo list of an employee """
import requests
import sys

userId = sys.argv[1]
r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
emp = r.json().get("name")
r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
		 .format(userId)).json()
total = len(r)
completed = []
for tasks in r:
    if tasks.get("completed"):
        completed.append(tasks)
com = len(completed)
print("Employee {} is done with tasks({}/{}):".format(emp, com, total))
for task in completed:
    print("\t{}".format(task.get("title")))
