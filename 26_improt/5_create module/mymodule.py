# ჩვენი მოდულის შექმნა

name = "Bob"

def hello():
    print("Hello", name)

def add_three_numbers(a, b, z):
    if a != 0 and b != 0 and z != 0:
        return a + b + z
    else:
        return "some is zero"
    

print(name)   
hello()
print(add_three_numbers(4,5,6))