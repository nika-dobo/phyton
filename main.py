
print("lern with: @itproge")
print("chanal link: https://www.youtube.com/@itproger")
print("video link: https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa&index=1 ")

print("")
print("")
print("")
print("")

# print("rezultati: ", 5, 7,  ".", sep="|", end="\n" ) 

# # sep
# # sep არის მზიიმის მერი დასორება და მაგ დაშორების მგაივრად რა შეგვიძლია ჩავსვათ. უნდა იყოს ბოლოში.
# # უნდა დაწერო , შემდეგ


# # end
# # end საშუალებით შეგვიძლია მივუთითოთ რა იქნება ხაზის ბოლოში
# # თუ /n ეს იქნება მშინ შემდეგ კოდს დაწერს ახალ ხაზზე
# # თუ სხვა რამეს მივუთითებთ(x) მაშინ წერის დროს x დაწერს პირველი პრინტის
# # შეგვიძლია გამოვიყნოთ ორივე ერთად x-ც და /n-ც
# # უნდა დაწერო , შემდეგ


# # \
# # როდესაც \ ამას ვიყენებთ ჩვენ ვეუბნებით რომ მაგლაითად " ეს იყოს ჩვეუებრივი სიმბოლო ანუ ათუ დავწერთ \" გამოიტანს: "
# print("hi \" hello")

# print("")

# # \n
# # არის ახალ ახზე გადასვლა კოდში. მაგ: 
# print("rez\nul\nta\nti:")

# print("")

# # \t
# # ტაბულაციის სიმბოლო ანი იგივე tab ოღნდ კოდში
# print("\trez\nul\nta\nti:")

# print("")

# # **
# # არის რიცხვის კავდრატში აყვანა
# print(5 ** 3)
# print(5 ** 2)

# print("")

# # //
# # თუ გაყოფის დორს არის ნაშთი მაშინ დაამგვალებს. ამგვალებს მიმიმალურამდე
# print(5 // 3)

# print("")

# # min()
# # ეძებს მიმიმალურ მნიშვნელობას მიცელულ რიცხვებში
# print(min(2, 43, 54, 32, 1, 4, 6, -5, -1, -12))

# print("")

# # max()
# # ეძებს მაქსიმალურ მნიშვნელობას მიცელულ რიცხვებში
# print(max(2, 43, 54, 32, 1, 4, 6, -5, -1, -12))

# print("")

# # abs()
# # ეძებს რიცხვის მოდულს, ანუ თუ უარყოფითია დაწერს დადებითს
# print(abs(-5))

# print("")

# #pow() = **
# print(pow(5, 3)) # 5-ის მგაივრად რიცხვი რომელიც გვინდა ავიყვანოთ კვადრატში. 3-ის მაგივრად რიცხვი რომელშიც გვინდა ავიყვანოთ პირველი როცხვი

# print("")

# #round() = //
# #ამგვალებს უახლოესთან
# print(round(5 / 3))

# print("")

# #del
# # ცვლადის წაშლა
# cvladi = 5
# del cvladi

# print("")

# #Ternary Operator
# data = input("number: ")
# number = 5 if data == "five" else 0
# print(number)

# # for
# for i in range(1, 6, 2):
#     print(i)
# # 1 ნიშნავს ეომ დათვლა დაიწყება 1 დან ანუ: 1, 2, 3, 4, 5,.2 ნიშნავს რომ 2-ით გაიზრდება ანუ: 0, 2, 4, 

# print("")

# # დათვლა რაიმეს დათვლა for-ში

# count = 0
# word = "hello world!"
# for i in word:
#     if i == "l":
#         count += 1  
# print(count)      

# print("")

# # while

# i = 3
# while i < 15:
#     print(i)
#     i += 2

#     print("")

# # სხვა მაგალითი | რომელიც ჯობია არ გაუშვა print-თან ერთად

# car = True

# while car:
#     if input("enter data: ") == "stop":
#         car = False

# print("")

# # brake და continue
# # brake არის ციკლიდან გამოსვლა. continue არის ციკლის გაგრზლება

# for i in range(15):
#     if i == 10:
#         break

#     if i % 2 == 0:
#         continue 

#     print(i)    

# print("")

# # ასოს სწორად პოვნა

# found = None
# for i in "hello":
#     if i == "l":
#         found = True
#         break

# else:
#     found = False
        
# print(found)
    
# print("")

# #list
# list = [5, 9, 56, 1, 2, 4, 6, 12]
# list.append(100)#ლისტში რაიმეს დამატება
# list.insert(1, 100) # insert-ის საშუალებით ვირჩევრ ინდექს და შემდეგ ვსვამთ რაც გვინდა. 1 არის ინდექსი ესეგი მერამდენი გვინდა იყო, 100 არის რაც გვინდა ჩავსვათ'
# list.extend([8, 4, 2, 63]) # extend რამოდენიმე რიცხვის ჩასმა ლისტში
# list.sort()# sort ალაგებს ლისტს ზრდადობით
# # list.reverse()#reverse ლისტს ატრიალებს
# list.pop()# შლის ბოლო ელემენტს
# list.remove(12)# წაშლის რასც მივუთითებთ
# # list.clear()# შლის ყველაფერს
# print(list)
# print(list.count(2))#count ითვლის რამდენია ამ ლისტში 2
# print(len(list))#ითვლის ლისტის მიგრძეს

# for i in list:
#     i *= 2
#     print(i)


# n = int(input("enter lenght: "))

# user_list = []

# i = 0
# while i < n:
#     string = "enter element  #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1

# print(user_list)


# print(" ")

# word = 'Football, basketball, skate'
# # print(word.count('!')) # ითვლის რამდენი ლიმბოლა სიტყვაში
# # print(word.capitalize()) # პირვე ასოს დიდად აქცევს
# # print(word.find('a')) #ეცებს a-ს
# hobby = word.split(', ') #აქცევს სტრინგს ლისტად

# for i in range(len (hobby)):
#     hobby[i] = hobby[i].capitalize()

# print(hobby)
# result = ", ".join(hobby)# join სტრინგში აერთიანებს
# print(result)


# #2 სხვა მაგალითი (ინდექსი და მოჭრა)

# word = "football"

# print(word[0:4])#მიმვამათავ იმ ელემენტამდე რომლემდეც მინდა გამოვიტანო. ამ შემთხვევაში მე-4 ასომდე.
# #[0:4] | 0 არის რომელი ელემნტიდან დაიწყოს ამ შემთხევევაში f-დან | 4 რამდენი სიმბოლო აიღოს ამ შემთხვევში foot 
# #ესეგი მე-0-ლე ელემენტიდან მე-4 ელემენტამდე

# print(word[4:8]) # აქ მე-4 ელემენტიდან მე-8 ელემენტამდე
# #ამის მეორე ვარიანტი
# print(word[4:])
# #ამის მესამე ვარიანტი
# print(word[4:-1])

# print(word[1:-1:2])# 2-ის საშუალებით 1 ელემენტს გამოვტოვებშ და შემდეგს დაპრინტაბს ანუ რამდენი რამდენი გამოტოვოს 


# #მეროე მაგალითის სხვა მაგალითი (ლისტი და მოჭრა)


# lis = [3, 5, "str", True, 5.3]

# print(lis[2::2])
# print(lis[::-1])



# #tuple
# #იგივე list მაგრამ ელემენტებს ვერ შევცვლით

# data = (3, 5, 13, 4, 3, True, "str", 6.5) 

# #data[4] = 6 #ერორი
# print(data[6])
# print(data[2:7:2])

# print(" ")

# print(data.count(3))
# print(len(data))
# print(data)

# print(" ")

# #tuple ვარიანტი 2

# data2 = 3, 4, 1, 2, 4, True, 4.5,
# print(data2)

# print(" ")

# data3 = (5)# ეს არ ითველბა როგორც tuple
# print(data3)

# data4 = (5,) #ასე ჩაითვლება როგორც tuple
# print(data4)

# data5 = 5,
# print(data5)

# #მაგალითები


# for i in data:
#     print(i)


# #როგორ გადავაქციოთ list-ი tuple-ში

# list = [4, 3, 5, 1]

# new_data = tuple(list)
# print(new_data)

# #როგორ გადავაქციოთ str-ი tuple-ში

# word = tuple("hello world")
# print(word)



# #dict
# #მსგავსია list-ისა და tuple-სი

# country = {2: "tbilisi", 4: "foti", 1: 34, 3: True, 8: 6.8, (3, 5): 6, True: False, "hi": "hello"}
# # x:y | x არის გასაღები ესეგი პრინტსი დროს თუ მივუწერთ x მაშინ დაიბედება y | ესეგი y არის სიტყვა რომელიც არის შენახული dict-ში
# #გასაღებად(x) შეგვიძლია გამოვიყენოთ tuple, bool, int, float და str. არ შეგვიძლია გამოვიყნოთ list-ი
# #country.clear() # შლის ყველაფერს dict-ში 
# country.pop("hi")#შილი იმას რომლის გასაღებს მივითითებთ
# country.popitem()#შლის ბოლო ელემენტს
# country[True] = True
# print(country)
# print(country[4])
# print(country.items())#გამოაქვს list-ი რომლის ყოველი ელემენტი არის tuple
# print(country.get(True))#გამოაქვს იმას რომლის გასაღებს მივუთითებთ
# print(country.keys())#მივიღებთ მხოლოდ გასაღებებს
# print(country.values())#მივიღებთ მხოლოდ მიშვნელობებს

# print(" ")

# for key in country:
#     print(key)
# #გამოიტანს გასაღებებს

# print(" ")

# for key, values in country.items():
#     print(key, "-", values)
# #გამოიტანს გასაღებსაც და ჩაწერილ სიტყვას


# #dict-ის მერორე ვარიანტი

# words = dict(code="geo", name="georgia",) #აქ გასღები უნდა იყოს დაწერილი სიტყვერად

# print(" ")

# #მაგალითი


# person = {
    
#     "user_1":{
#         "first_name": "nika",
#         "last_name": "dobo",
#         "age": 16,
#         "addres":["aqlaqi", "rainoi", "misamarti"],
#         "grades":{
#             "qartuli": 8,
#             "matematika": 9,
#             "rusuli": 10,
#             "inglisuri": 9,
#             "qimia": 10,
#         }
#     },
#     "user_2":{
#         "first_name": "gabriel",
#         "last_name": "molodini",
#         "age": 30,
#         "addres":["aqlaqi", "rainoi", "misamarti"],
#         "grades":{
#             "qartuli": 2,
#             "matematika": 2,
#             "rusuli": 2,
#             "inglisuri": 2,
#             "qimia": 2,
#         }
#     }    
# }
# print(person["user_1"]["grades"]["matematika"])


# #set და frozenset
# #არის მსაგავსი list-ის და tuple-ის ნაირი. მაგრამ ერთნაირი ელემენტები იშლება
# #მაგრამ ჩაწერილი ელემტები იქნება არეული გამოყვანის დროს

# #set
# #შეგვიძლია შევცვალოთ ელემენტები და შეგვიძლა დავამატოთ ელემნტები 

# data = set("hello")
# print(data)

# print(" ")

# data2 = {2, 4, 2, 4, 6, 3, 7, 1, 7, 8 }
# data2.add(43)# 1 ელემენტის დამატება
# data2.update(34, True, 4.8)# რამდენიმე ელემნტის დამატება
# data2.remove(True)#წაშლა იმ ელემენტის რომელსაც მივუთითებს
# data2.pop()#ბოლო ელემენტის წაშლა
# #data2.clear()#მთლიანად წაშლა
# print(data2)

# nums = [2, 4, 2, 6, 7, 43, 85, 8]
# nums = set(nums)#list-ს ვაქცევს setად


# #frozenset
# #არ შეგვიძლია შევცვალოთ ელემნტები და არ შეგვიძლა დავამატოთ ელემნტები


# new_data = frozenset([2, 4, 2, 4, 6, 3, 7, 1, 7, 8, 2, 4, 2, 6, 7, 43, 85, 8, True, "hello"])
# print(new_data)


# #def და lambda

# #def
# #ფნქციის შექმნა

# def test_func(word):
#     print(word, end="")
#     print("!")

# test_func("hi") 
# test_func(5) 

# print(" ")

# def summa(a, b):
#     res = a + b
#     print("result:", res)

# summa(5, 6)
# summa("h", "i")  

# print(" ")

# def summa2(a, b):
#     return  a + b

# res = summa2(5, 2)
# print(res)

# print(summa("h", "i"))  

# print(" ")

# #მაგალითი

# #def-ის გარაშე

# num = [1, 4, 6, 2, 7, 3, 7, 3, 5]
# num2 = [1.5, 4.2, 6.67, 2.2, 7.5, 3.9, 7.4, 3.6, 5.4]

# min = num[0]   
# for i in num:
#     if i < min:
#         min = i

# print(min)        

# min2 = num2[0]   
# for i in num2:
#     if i < min2:
#         min2 = i

# print(min2) 

# print(" ")

# #def-ის საშუალებით


# def minimal(l):
#     min_num = l[0]
#     for i in l:
#         if i < min_num:
#             min_num = i

#     print(min_num)      


# minimal(num)
# minimal(num2)


# print(" ")

# #lambda
# #ანონიმური ფუნქცია

# func = lambda x, y: x * y 
# print(func(5, 3))

# resu = func(5, 5)
# print(resu)


# #work with file


# data = input("whrite text:")

# file = open("data/text.txt", "w")#იხსნება ფაილი და თუ არ გაქ შექმნილი მაშინ შეიქმნება

# # w - წერის გახსნა, ფაილის შინაარსი წაიშლება, თუ ფაილი არ არსებობს, იქმნება ახალი.
# # r - გახსენით კითხვისთვის (არის ნაგულისხმევი მნიშვნელობა).
# # x - გახსენით წერა, თუ ფაილი არ არსებობს, წინააღმდეგ შემთხვევაში გამონაკლისი დააგდეს.
# # a - გახსნა უნდა ჩაიწეროს, ინფორმაცია ემატება ფაილის ბოლოს.
# # b - გახსნა ორობითი რეჟიმში.
# # t - ტექსტის რეჟიმში გახსნა (არის ნაგულისხმევი მნიშვნელობა).
# # + - კითხვისა და წერის გახსნა

# file.write(data + "\n")
# file.write("!!!")

# file.close()

# print(" ") 

# file = open("data/text.txt", "r")

# print(file.read())# თუ მივუთითებთ პარამეტრებს ფჩხილებში მაშინ მაგდენ სიმბლოს გამოიტასნ და თუ ცარიელია მაშინ ყველაფერს გამოიტანს

# print(" ") 


# for line in file:
#     print(line, end="")


# file.close()


# #try end except


# try:
#     x = int(input("enter number: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("enter better number!")


# y = 0

# while y == 0:
#     try:
#         y = int(input("enter number: "))
#         y += 5
#         print(x)
#     except ValueError:
#         print("enter better number!")


# try:
#     c = 5 / 0
#     c = int(input("enter number: "))
# except ZeroDivisionError:
#     print("you cent / on 0")
# except ValueError:
#     print("enter better number!")   
# else:
#     print("else")    
# finally:
#     print("finally")        


# # with და as
# #იგივე არის რაც .close()    

# try:
#     with open("text2.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file not founded")        
        
# print(" ") 

# # import


# import time # ამას შემოყავს დროსთან დაკავშირებული კოდი import არის შემოტანა რომ კოდმა დაინახოს შემდეგ time არის მოდული რომელიც შემოგყვავს

# time.sleep(5) # 5 წამით ყინავს პროგრამას ანუ ამის შემდეგ 5 წამი უნდა გავიდეს რომ დაიწეროს ამის შემდგომი კოდი
# print("hello world!")

# print(" ") 

# import datetime as d # as d არის სახელი რომელიაც შევძლებს გამოძახებას (არ არის აუცილებელი)

# print(d.datetime.now().time().hour) #ამ კოდით გვიბრუნებს დროს ამ შემთხვევში საათს
# print(d.datetime.now().time())# ეს დააბრუნებს ახლანდელ დროს (საათს, წუთს, წამს,)
# print(d.datetime.now()) # ეს აბრუნებს ახლანდელ დროს და თარიღს(წელს, თვეს, დღეს, საათს, წუთს, წამს,)

# print(" ") 

# import time, datetime as d, sys, os, platform # , შექგვიძლია გამოვყოთ ერთმანეთისგან რამოდენიმე მოდილი ესეგი ამის გამო შევიძლეა 1 ხაზში დავაიმპორტიროთ(დავამატოთ) რამოდენიმე მოდული

# print(d.datetime.now().time().hour)

# print(sys.path)# ეს არის sys-ს. ეს ფუნქცია გვიჩვენებს რა გაზა უნდა გამიაროს ამ ფაილამდე რომ რამე დაპრინტოს ამ ფაილში

# print(os.name)# ეს გვიჩვენებს ოპერაციული სისტემის სახელს ოღონდ გამოყავს ცოტა უცნაყრად(მაგ: nt, posix)

# print(platform.system())# ეს გვიჩვენებს ოპერაციული სისტემის სახელს (მაგ: Windows, Linux, Mac)

# print(" ") 

# from math import sqrt as s, ceil  # ამ შემტხვევში ჩვენ შემოგვყავს მხოლოდ sqrt და ceil ფუნქცია math-იდან

# # sqrt ეს ფუქნცია პოულობს რიცხვის კვადრატულ ფესვს
# # ceil ეს ფუნქცია ამგვალებს რიცხვს

# print(ceil(s(100)))

# print(" ") 

# # mymodule # ჩვენი მოდულის შექმნა

# name = "Bob"

# def hello():
#     print("Hello", name)

# def add_three_numbers(a, b, z):
#     if a != 0 and b != 0 and z != 0:
#         return a + b + z
#     else:
#         return "some is zero"

# import mymodule as my

# print(name)

# my.hello()

# my.add_three_numbers(5, 6, 7)

