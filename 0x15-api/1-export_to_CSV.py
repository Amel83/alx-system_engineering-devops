#!/usr/bin/python3
"""Exports to-do list info"""


import csv
import requests
import sys

if __name__ == "__main__":
    idd = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(idd)).json()
    username = user.get("username")
    todo = requests.get(url + "todo", params={"userId": user_id}).json()
    with open("{}.csv".format(idd), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [idd, username, t.get("completed"), t.get("title")]
         ) for t in todo]
