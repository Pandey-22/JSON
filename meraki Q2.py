# python object ko json data me convert kare

import json
python_object={
    "name":"David",
    "class":"I",
    "age":6
}
print(type(python_object))
# o/p=<class 'dict'>
j_data=json.dumps(python_object)
print(j_data)
# o/p={"name":"David","class":"I","age":6}
print(type(j_data))
# o/p=<class 'str'>