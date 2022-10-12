import json

input = '''{"name": "Bond", "Phone":{"type":"intl", "number":"007"}, "email": {"hide": "yes"}}'''

d= json.loads(input)

print(d['name'])
print(d['Phone']['number'])
