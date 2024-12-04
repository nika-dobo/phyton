
#list


list = [5, 9, 56, 1, 2, 4, 6, 12]
list.append(100)#ლისტში რაიმეს დამატება
list.insert(1, 100) # insert-ის საშუალებით ვირჩევრ ინდექს და შემდეგ ვსვამთ რაც გვინდა. 1 არის ინდექსი ესეგი მერამდენი გვინდა იყო, 100 არის რაც გვინდა ჩავსვათ'
list.extend([8, 4, 2, 63]) # extend რამოდენიმე რიცხვის ჩასმა ლისტში
list.sort()# sort ალაგებს ლისტს ზრდადობით
# list.reverse()#reverse ლისტს არევა
list.pop()# შლის ბოლო ელემენტს
list.remove(12)# წაშლის რასც მივუთითებთ
# list.clear()# შლის ყველაფერს
print(list)
print(list.count(2))#count ითვლის რამდენია ამ ლისტში 2
print(len(list))#ითვლის ლისტის სიგრძეს

print(" ")

for i in list:
    i *= 2
    print(i)


print(" ")

#მაგალითი

n = int(input("enter lenght: "))

user_list = []

i = 0
while i < n:
    string = "enter element  #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)


print(" ")

#სხვა მაგალითი და +კოდიც

word = 'Football, basketball, skate'
# print(word.count('!')) # ითვლის რამდენი სიმბოლა სიტყვაში
# print(word.capitalize()) # პირვე ასოს დიდად აქცევს
# print(word.find('a')) #ეცებს a-ს | ეძებს იმას რასაც ჩავწერთ ("")-აქ
hobby = word.split(', ') #აქცევს სტრინგს ლისტად

for i in range(len (hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)