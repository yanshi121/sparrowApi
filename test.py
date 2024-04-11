import inspect
import time
import json
import requests
import datetime
# a = requests.get('http://127.0.0.1:7012/', data={'name': 'sex', "id": 2})
# print(a.status_code)
# print(a.text)
# print(a.headers)
# a = requests.post("http://127.0.0.1:7012/", data={"command": "set name sex 5.5"})
# print(a.status_code)
# print(a.text)
# time.sleep(5)
# a = requests.post("http://127.0.0.1:712", data={"command": "set_body name name=bob,sex=male,age=0"})
# print(a.status_code)
# print(a.text)
# a.close()
# a = requests.post("http://127.0.0.1:712", data={"command": "set_body_time name 6"})
# print(a.status_code)
# print(a.text)
# a.close()
print(sorted(['data', 'headers']) == sorted(["data", "args"]))

