import json 
s={1:2,3:5}
f=open('WJF.json','w')
v=json.dump(s,f,indent=1)
print(v)