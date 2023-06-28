import json
x={
    "name":"Ken",
    "age":45,
    "married":True,
    "children":("Alice","Bob"),
    "pets":["Dog"],
    "cars":[
        {"modal":"Audi AI","mpg":15.1},
        {"modal":"Zeep Compass","mpg":18.1}
    ]
}
sorted_str=json.dumps(x,indent=4,sort_keys=True)
print(sorted_str)