#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(sys.argv[1]), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(sys.argv[1])).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user.get("id"), user.get("username"),
                             task.get("completed"), task.get("title")])
