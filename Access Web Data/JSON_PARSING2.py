import json

input = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    {
      "id" : "009",
      "x" : "56",
      "name" : "Bren"
    }
]'''

info = json.loads(input)
print("User Count:", len(info))

for user in info:
    print("Name:", user["name"])
    print("ID:", user["id"])
    print("Attribute:", user["x"])