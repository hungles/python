fruits = ("banana", "apple", "orange")

myiter = iter(fruits)

print(next(myiter))
print(next(myiter))
print(next(myiter))

class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
number = myNumbers()

numbers = iter(number)

for i in numbers:
    print(i)


