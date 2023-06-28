# Read JSON file

# import json
# file=open("RJF.json","r")
# x=file.read()
# # print(x)
# final_d=json.loads(x)
# print(final_d)
# print(type(final_d))


# import json
# file=open("RJF.json","r")
# x=file.read()
# final_d=json.loads(x)
# for a in final_d:
#     print(a)



import json
file=open("RJF.json","r")
x=file.read()
final_d=json.loads(x)
for a in final_d:
    print(a['Name'],a["Sarname"],a["Age"],a["Relation"])