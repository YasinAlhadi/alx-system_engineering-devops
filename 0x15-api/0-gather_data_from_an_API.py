#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
import sys

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(sys.argv[1]), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(sys.argv[1])).json()
    completed_task = []
    for task in todo:
        if task.get("completed") is True:
            completed_task.append(task.get("title"))
    completed_task_tit = "\n".join(completed_task)
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed_task), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_task))
