#Inheritance encapsulation polymorphism

class building:
    __year = None
    __city = None
    # __ ეს არის დაცვა მაგრამ კარგად არ არის გაკეთბული encapsulation

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("year:", self.year, "city:", self.city)

class shool(building):
    pupiles = 0

    def __init__(self, year, city, pupiles):#Inheritance
        super(school, self).__init__(year, city)# ამითი ვეხმიანებით მთავარ კლასს ანუ მშობელ კლას რომ მის პარამეტრები მივიღოთ 
        self.pupiles = pupiles

    def get_info(self):
        super().get_info()# aაქ შეგვიძლია დავწეროთ ასე print("year:", self.year, "city:", self.city)
        print("pupiles:", self.pupiles)#polymorphism

    

class house(building):# აქ თუ building ამის მაგივრად მივუთითებთ shool მაშინ შეხება გვექნებ shool ნაც და building ნაც
    pass

class shop(building):
    pass

school = building(100, 1990, "tbilisi")
house = building(2000, "batumi")
shop = building(2010, "kutaisi")