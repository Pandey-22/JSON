# Q7..text file data ko json file data me convert kare
import json 
json_file_data={
    "Name":"Abhishek",
    "Designation":"CEO of navgurukul",
    "Gender":"male",
    "Age":"29"
}
a=json.dumps(json_file_data)
print(a)