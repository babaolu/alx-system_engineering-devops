#!/usr/bin/python3
""" Displays todo list of an employee """
if __name__ == "__main__":
    import json
    import requests

    r = requests.get("https://jsonplaceholder.typicode.com/users")
    todolist = {}
    for user in r.json():
        emp = user.get("username")
        ts = requests.get("https://jsonplaceholder.typicode.com/todos?" +
                          "userId={}".format(user.get("id"))).json()
        dictlist = [{"username": emp, "task": x.get("title"), "completed":
                    x.get("completed"), "username": emp} for x in ts]
        todolist.update({user.get("id"): dictlist})
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todolist, jsonfile)
