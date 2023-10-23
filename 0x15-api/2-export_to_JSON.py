#!/usr/bin/python3
"""Exports to-do list info in JSon format"""


import json
import requests
import sys

if __name__ == "__main__":
    idd = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todo", params={"userId": idd}).json()
    with open("{}.json".format(idd), "w") as jsonfile:
        json.dump({idd: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo]}, jsonfile)
