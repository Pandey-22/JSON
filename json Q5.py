import json
x={
    "name":"john",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"modal":"BMW 230","mpg":27.5},
        {"modal":"Ford Edge","mpg":24.1}]}
y=json.dumps(x)
print(y)