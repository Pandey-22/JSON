# Q4..python dictionary(sort by key) object ko json data me convert kare
import json
a={
    '4':5,
    '6':7,
    '1':3,
    '2':4}
print(type(a))
# o/p=<class 'dict'>
j_data=json.dumps(a)
print(j_data)
# o/p={"4":5, "6":7, "1":3, "2":4}
print(type(j_data))
# o/p=<class 'str'>