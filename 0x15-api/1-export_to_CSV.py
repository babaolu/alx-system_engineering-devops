#!/usr/bin/python3
""" Displays todo list of an employee """
import csv
import requests
import sys

userId = sys.argv[1]
r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                 .format(userId))
emp = r.json().get("username")
r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                 .format(userId)).json()

with open("{}.csv".format(userId), "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in r:
        spamwriter.writerow([userId, emp, task.get("completed"),
                            task.get("title")])
