# import json
# a={
#     "shopping_list":
#         {
#             "choco":"15",
#             "biscuits":"50",
#             "dairymilk":"30",
#             "ice_cream":"20"
#         }
# }
# z=json.dumps(a)
# print(z)
# print(type(z))


# import json 
# a={"shopping_list":{"choco":"50",
#                     "biscuits":"50",
#                     "ice_cream":"50"}}
# items=input("enter the items:-")
# quantity=int(input("how much you want to buy"))
# b=a["shopping_list"][items]
# c=int(b)-quantity
# a["shopping_list"][items]=c
# print(a)