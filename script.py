import math
import sys
from os import rename

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeting = "Helo, {}".format(who_to_greet)
    return greeting


r = requests.get("https://hackeny.com")
print(r.status_code)

# for get text from terminal
name = input("Your Name? ")
print("Hello,", name)
