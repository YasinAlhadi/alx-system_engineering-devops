#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(sys.argv[1]), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(sys.argv[1])).json()
    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump({user.get("id"): [{"task": task.get("title"),
                                     "completed": task.get("completed"),
                                     "username": user.get("username")}
                                    for task in todo]}, json_file)
