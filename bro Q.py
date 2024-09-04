# import array as arr 
# arr=[
#   {'id':1,'name':'John'},
#   {'id':2,'name':'Jane'},
#   {'id':3,'name':'John'},
#   {'id':4,'name':'Jack'},
#   {'id':2,'name':'Jane'},
# ]
# arr.remove({'id':2,'name':'Jane'})
# arr.remove({'id':2,'name':'Jane'})
# print(arr)



# arr=[
#   {'id':1,'name':'John'},
#   {'id':2,'name':'Jane'},
#   {'id':3,'name':'John'},
#   {'id':4,'name':'Jack'},
#   {'id':2,'name':'Jane'},
# ]
# for i in arr.copy():
#     if i.get('id')==2:
#         arr.remove(i)
#         break
# print(arr)


# arr=[
#   {'id':1,'name':'John'},
#   {'id':2,'name':'Jane'},
#   {'id':3,'name':'John'},
#   {'id':4,'name':'Jack'},
#   {'id':2,'name':'Jane'},
# ]
# for i in range(len(arr)):
#     if arr[i]['id']==2:
#         del arr[i]
#         del arr[i+2]
#         break
# print(arr)