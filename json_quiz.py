import json

str= '''{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}'''

js= json.loads(str)

print(js)
