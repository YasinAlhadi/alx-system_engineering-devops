#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    user_dict = {}
    user_name_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        user_name_dict[user_id] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in todo:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["username"] = user_name_dict.get(user_id)
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        user_dict.get(user_id).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
