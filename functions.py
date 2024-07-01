def say_hello():
    print("Hello!")

def sum(a,b):
    return a+b

def avg(a,b):
    return (a+b)/2

def name(first_name, last_name):
    return f"{last_name}, {first_name}"


def list(first, last, year, student_num):
    return[first, last, year, student_num]

def over_18(a):
    return a > 18

def reverse(word):
    print(word[::-1])


say_hello()
print(sum(3,4))
print(avg(6,2))
print(name("Kayla", "Tapiador"))
print(list("Kayla", "Tapiador", 2015, 123456))
print(over_18(17))
print(over_18(25))
reverse("ice")
