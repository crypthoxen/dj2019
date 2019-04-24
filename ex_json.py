import json
json_data=open('j.json').read()

data = json.loads(json_data)
print(data)
f = open('jdump.txt','w')
json.dump(data,f)
f.close()
