#!/usr/bin/python3
"""Returns to-do list info"""


import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todo", params={"userId": sys.argv[1]}).json()
    complete = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todo)))
    [print("\t {}".format(c)) for c in complete]
