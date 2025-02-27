class cat:
    name = None
    age = None
    ishappy = None

    def __init__(self, name, age, ishappy):# ამ ფუნქციაში შევქმენით ცვლადები რომლებიც შემოვიტანეთ კლასის შექმნის დროს და შევინახეთ მათ მნიშვნელობები და გამოძახების დროს როდესაც ვუთითებთ ნებისმერ ცვლადს მა კლასს შეგვიძლია პირდაპირ კლასში მოხუთითოთ ყველაფერი
        # self.name = name
        # self.age = age
        # self.ishappy = ishappy

        self.set_data(name = None, age = None, ishappy = None) # ამ None დახმარებით შეგვიძლია მაოვიძახოთ 0 ან 1 ან 2 ხვალადი ერორის გამრეშე ეს შეგვიძლია მამოვიენოთ __init__ შიც მაგრამ None მაგივრად სხვა რემეც შეგვიძლია მივუთითოთ

        self.get_data()

    def set_data(self, name, age, ishappy):
        self.name = name
        self.age = age
        self.ishappy = ishappy

    def get_data(self):
        print("name:", self.name, "age:", self.age, "ishappy:", self.ishappy)

cat1 = cat("jopa", 3, True)



cat2 = cat("barsik", 5, False)