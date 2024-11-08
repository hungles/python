thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["year"])

print(thisdict.get("model"))

print(thisdict.keys())

thisdict["color"] = "Red"

print(thisdict.keys())


print(thisdict.values())

thisdict["year"] = 1990

print(thisdict.values())

print(thisdict.items())