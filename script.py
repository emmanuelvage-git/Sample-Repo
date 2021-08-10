import requests


r = requests.get("https://hackeny.com")
print(r.status_code)
print(r.ok)
