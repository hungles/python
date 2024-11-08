myDictio = {
    "Name" : "Juan",
    "Lastname": "Perez",
    "email" : "jperez@gmail.com",
    "years": 30
}

for i in myDictio:
    print(myDictio[i])

print(myDictio.values())

for i in myDictio.values():
    print(i)

print(myDictio.items())

for x, y in myDictio.items():
    print(x, y)