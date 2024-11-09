def print_variable():
    x = 300
    print(x)

print_variable()

def variable_inside_function():
    x = 200

    def print_inside():
        print(x)

    print_inside()

variable_inside_function()

def global_variable():
    global x
    x = 300

global_variable()    

try:
    print(x, "desde el try")
except:
    print("The variable x it´s not defined!!")

