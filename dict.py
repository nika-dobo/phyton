
#dict
#მსგავსია list-ისა და tuple-სი

country = {2: "tbilisi", 4: "foti", 1: 34, 3: True, 8: 6.8, (3, 5): 6, True: False, "hi": "hello"}
# x:y | x არის გასაღები ესეგი პრინტსი დროს თუ მივუწერთ x მაშინ დაიბედება y | ესეგი y არის სიტყვა რომელიც არის შენახული dict-ში
#გასაღებად(x) შეგვიძლია გამოვიყენოთ tuple, bool, int, float და str. არ შეგვიძლია გამოვიყნოთ list-ი
#country.clear() # შლის ყველაფერს dict-ში 
country.pop("hi")#შილი იმას რომლის გასაღებს მივითითებთ
country.popitem()#შლის ბოლო ელემენტს
country[True] = True
print(country)
print(country[4])
print(country.items())#გამოაქვს list-ი რომლის ყოველი ელემენტი არის tuple
print(country.get(True))#გამოაქვს იმას რომლის გასაღებს მივუთითებთ
print(country.keys())#მივიღებთ მხოლოდ გასაღებებს
print(country.values())#მივიღებთ მხოლოდ მიშვნელობებს

print(" ")

for key in country:
    print(key)
#გამოიტანს გასაღებებს

print(" ")

for key, values in country.items():
    print(key, "-", values)
#გამოიტანს გასაღებსაც და ჩაწერილ სიტყვას


#dict-ის მერორე ვარიანტი

words = dict(code="geo", name="georgia",) #აქ გასღები უნდა იყოს დაწერილი სიტყვერად

print(" ")

#მაგალითი


person = {
    
    "user_1":{
        "first_name": "nika",
        "last_name": "dobo",
        "age": 16,
        "addres":["aqlaqi", "rainoi", "misamarti"],
        "grades":{
            "qartuli": 8,
            "matematika": 9,
            "rusuli": 10,
            "inglisuri": 9,
            "qimia": 10,
        }
    },
    "user_2":{
        "first_name": "gabriel",
        "last_name": "molodini",
        "age": 30,
        "addres":["aqlaqi", "rainoi", "misamarti"],
        "grades":{
            "qartuli": 2,
            "matematika": 2,
            "rusuli": 2,
            "inglisuri": 2,
            "qimia": 2,
        }
    }    
}
print(person["user_1"]["grades"]["matematika"])
