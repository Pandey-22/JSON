# Q1..json data ko python object me convert kare

import json
json_object='{"Name":"David","Class":"I","Age":6}'
print(type(json_object))
# o/p=<class 'str'>
python_object=json.loads(json_object)
print(python_object)
# o/p={'Name':'David','Class':'I','Age':6}
print(type(python_object))
# o/p=<class 'dict'>