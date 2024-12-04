
#def და lambda

#def
#ფნქციის შექმნა

def test_func(word):
    print(word, end="")
    print("!")

test_func("hi") 
test_func(5) 

print(" ")

def summa(a, b):
    res = a + b
    print("result:", res)

summa(5, 6)
summa("h", "i")  

print(" ")

def summa2(a, b):
    return  a + b

res = summa2(5, 2)
print(res)

print(summa2("h", "i"))  

print(" ")

#მაგალითი

#def-ის გარაშე

num = [1, 4, 6, 2, 7, 3, 7, 3, 5]
num2 = [1.5, 4.2, 6.67, 2.2, 7.5, 3.9, 7.4, 3.6, 5.4]

min = num[0]   
for i in num:
    if i < min:
        min = i

print(min)        

min2 = num2[0]   
for i in num2:
    if i < min2:
        min2 = i

print(min2) 

print(" ")

#def-ის საშუალებით


def minimal(l):
    min_num = l[0]
    for i in l:
        if i < min_num:
            min_num = i

    print(min_num)      


minimal(num)
minimal(num2)


print(" ")

#lambda
#ანონიმური ფუნქცია

func = lambda x, y: x * y 

print(func(5, 3))

resu = func(5, 5)
print(resu)
