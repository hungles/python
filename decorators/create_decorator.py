def myDecorator(func):
    def decorator_function():
        print("Before the function")
        func()
        print("After the function")
    return decorator_function

@myDecorator
def hello():
    print("Hello World")

hello()