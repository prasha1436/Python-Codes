import json

input = '''[{"ID": "007", "x":"1", "name":"Bond"},{"ID": "111", "x":"2", "name":"Equalizer"}]'''

l= json.loads(input)
print('Count:', len(l))
for item in l:
    print(item["x"])
    print(item["name"])
    print(item["ID"])
