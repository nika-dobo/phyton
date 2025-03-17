
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

words = 'FootBall, basKetball, skAte'
# print(word.count('!')) # ითვლის რამდენი სიმბოლა სიტყვაში
# print(word.capitalize()) # პირვე ასოს დიდად აქცევს
# print(word.find('a')) #ეცებს a-ს | ეძებს იმას რასაც ჩავწერთ ("")-აქ
hobby = words.split(', ') #აქცევს სტრინგს ლისტად

for i in range(len (hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)
result = ", ".join(hobby)# join სტრინგში აერთიანებს
print(result)


#2 სხვა მაგალითი (ინდექსი და მოჭრა)

word = "football"

print(word[0:4])#მიმვამათავ იმ ელემენტამდე რომლემდეც მინდა გამოვიტანო. ამ შემთხვევაში მე-4 ასომდე.
#[0:4] | 0 არის რომელი ელემნტიდან დაიწყოს ამ შემთხევევაში f-დან | 4 რამდენი სიმბოლო აიღოს ამ შემთხვევში foot 
#ესეგი მე-0-ლე ელემენტიდან მე-4 ელემენტამდე

print(word[4:8]) # აქ მე-4 ელემენტიდან მე-8 ელემენტამდე
#ამის მეორე ვარიანტი
print(word[4:])
#ამის მესამე ვარიანტი
print(word[4:-1])

print(word[1:-1:2])# 2-ის საშუალებით 1 ელემენტს გამოვტოვებშ და შემდეგს დაპრინტაბს ანუ რამდენი რამდენი გამოტოვოს 


#მეროე მაგალითის სხვა მაგალითი (ლისტი და მოჭრა)


lis = [3, 5, "str", True, 5.3]

print(lis[2::2])
print(lis[::-1])

#.translate()შლის ყველა სიმბოლოს რომელიც მითითებულია
#მაგალითი
print(" ")
string = "hello world"
print(string.translate({ord("h"): None, ord("l"): None}))


#.endswith() ამოწებს რომელი სიმბოლოთი დასრულდა სტრინგი
#მაგალითი
print(" ")
string = "hello world"
print(string.endswith("d"))