# Definition

def say_hello():
    print("Hello World!")

say_hello()
say_hello()

print("Hello Emmanuel")
print("Hello Oiza")
print("Hello Oluchi")

def greet(name):
    print("Hello", name)

greet("Emmanuel")
greet("Oiza")
greet("Oluchi")


def add(a,b):
    print("sum:", a+b)

add(3,5)

def greet(name = "Guest"):
    print("Hello", name)

greet("Emmanuel")
greet()

def square(num):
    return num * num

result = square(4)
print("Square of 4 is:", result)


