print("rezultati: ", 5, 7,  ".", sep="|", end="\n" ) 

# sep
# sep არის მზიიმის მერი დასორება და მაგ დაშორების მგაივრად რა შეგვიძლია ჩავსვათ. უნდა იყოს ბოლოში.
# უნდა დაწერო , შემდეგ


# end
# end საშუალებით შეგვიძლია მივუთითოთ რა იქნება ხაზის ბოლოში
# თუ /ნ ეს იქნება მშინ შემდეგ კოდს დაწერს ახალ ხაზზე
# თუ სხვა რამეს მივუთითებთ(x) მაშინ წერის დროს x დაწერს პირველი პრინტის
# შეგვიძლია გამოვიყნოთ ორივე ერთად x-ც და /n-ც
# უნდა დაწერო , შემდეგ


# \
# როდესაც \ ამას ვიყენებთ ჩვენ ვეუბნებით რომ მაგლაითად " ეს იყოს ჩვეუებრივი სიმბოლო ანუ ათუ დავწერთ \" გამოიტანს: "
print("hi \" hello")

print("")

# \n
# არის ახალ ახზე გადასვლა კოდში. მაგ: 
print("rez\nul\nta\nti:")

print("")

# \t
# ტაბულაციის სიმბოლო ანი იგივე tab ოღნდ კოდში
print("\trez\nul\nta\nti:")

print("")

# **
# არის რიცხვის კავდრატში აყვანა
print(5 ** 3)
print(5 ** 2)

print("")

# //
# თუ გაყოფის დორს არის ნაშთი მაშინ დაამგვალებს. ამგვალებს მიმიმალურამდე
print(5 // 3)

print("")

# min()
# ეძებს მიმიმალურ მნიშვნელობას მიცელულ რიცხვებში
print(min(2, 43, 54, 32, 1, 4, 6, -5, -1, -12))

print("")

# max()
# ეძებს მაქსიმალურ მნიშვნელობას მიცელულ რიცხვებში
print(max(2, 43, 54, 32, 1, 4, 6, -5, -1, -12))

print("")

# abs()
# ეძებს რიცხვის მოდულს, ანუ თუ უარყოფითია დაწერს დადებითს
print(abs(-5))

print("")

#pow() = **
print(pow(5, 3)) # 5-ის მგაივრად რიცხვი რომელიც გვინდა ავიყვანოთ კვადრატში. 3-ის მაგივრად რიცხვი რომელშიც გვინდა ავიყვანოთ პირველი როცხვი

print("")

#round() = //
#ამგვალებს უახლოესთან
print(round(5 / 3))

print("")

#del
# ცვლადის წაშლა
cvladi = 5
del cvladi

print("")

#Ternary Operator
data = input("number: ")
number = 5 if data == "five" else 0
print(number)

# for
for i in range(1, 6, 2):
    print(i)
# 1 ნიშნავს ეომ დათვლა დაიწყება 1 დან ანუ: 1, 2, 3, 4, 5,.2 ნიშნავს რომ 2-ით გაიზრდება ანუ: 0, 2, 4, 

print("")

# დათვლა რაიმეს დათვლა for-ში

count = 0
word = "hello world!"
for i in word:
    if i == "l":
        count += 1  
print(count)      

print("")

# while

i = 3
while i < 15:
    print(i)
    i += 2

    print("")

# სხვა მაგალითი | რომელიც ჯობია არ გაუშვა print-თან ერთად

car = True

while car:
    if input("enter data: ") == "stop":
        car = False

print("")

# brake და continue
# brake არის ციკლიდან გამოსვლა. continue არის ციკლის გაგრზლება

for i in range(15):
    if i == 10:
        break

    if i % 2 == 0:
        continue 

    print(i)    

print("")

# ასოს სწორად პოვნა

found = None
for i in "hello":
    if i == "l":
        found = True
        break

else:
    found = False
        
print(found)
    
print("")

#list
list = [5, 9, 56, 1, 2, 4, 6, 12]
list.append(100)#ლისტში რაიმეს დამატება
list.insert(1, 100) # insert-ის საშუალებით ვირჩევრ ინდექს და შემდეგ ვსვამთ რაც გვინდა. 1 არის ინდექსი ესეგი მერამდენი გვინდა იყო, 100 არის რაც გვინდა ჩავსვათ'
list.extend([8, 4, 2, 63]) # extend რამოდენიმე რიცხვის ჩასმა ლისტში
list.sort()# sort ალაგებს ლისტს ზრდადობით
# list.reverse()#reverse ლისტს ატრიალებს
list.pop()# შლის ბოლო ელემენტს
list.remove(12)# წაშლის რასც მივუთითებთ
# list.clear()# შლის ყველაფერს
print(list)
print(list.count(2))#count ითვლის რამდენია ამ ლისტში 2
print(len(list))#ითვლის ლისტის მიგრძეს

for i in list:
    i *= 2
    print(i)


n = int(input("enter lenght: "))

user_list = []

i = 0
while i < n:
    string = "enter element  #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)


print(" ")

word = 'Football, basketball, skate'
# print(word.count('!')) # ითვლის რამდენი ლიმბოლა სიტყვაში
# print(word.capitalize()) # პირვე ასოს დიდად აქცევს
# print(word.find('a')) #ეცებს a-ს
hobby = word.split(', ') #აქცევს სტრინგს ლისტად

for i in range(len (hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)

