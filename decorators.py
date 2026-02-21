


def decorator(addition):
    def wrapper(a,b):
        print("let start")
        result = addition(a,b)
        print(result)
        print("this is the addition to the number you have given")
        return result
    return wrapper

@decorator
def addition(a,b):
    return a+b

a= int(input("number"))
b=int(input("second"))
addition(a,b)