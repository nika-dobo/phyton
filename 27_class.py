class cat:
    name = None
    age = None
    ishappy = None

    def set_data(self, name, age, ishappy):
        self.name = name
        self.age = age
        self.ishappy = ishappy

    def get_data(self):
        print("name:", self.name, "age:", self.age, "ishappy:", self.ishappy)

cat1 = cat()
cat1.set_data("jopa", 3, True)


cat2 = cat()
cat2.set_data("barsik", 5, False)

cat1.get_data()
cat2.get_data()