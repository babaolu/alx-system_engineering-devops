#!/usr/bin/python3
""" Displays todo list of an employee """
if __name__ == "__main__":
    import json
    import requests
    import sys

    userId = sys.argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(userId))
    emp = r.json().get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                     .format(userId)).json()

    dictlist = [{"task": x.get("title"), "completed": x.get("completed"),
                "username": emp} for x in r]
    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: dictlist}, jsonfile)
