fruits = ["banana", "kiwi", "apple", "orange", "melon", "watermelon"]

print(fruits)

fruits.sort()

print(fruits)

fruits.sort(reverse= True)

print(fruits)

def rest50(x):
    return abs(x - 50)

numbers = [50, 10, 25, 100, 135]

numbers.sort(key = rest50)

print(numbers)