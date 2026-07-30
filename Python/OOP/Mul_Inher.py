class Mother:
    def skill1(self):
        print("Mother is Cooking")

class Father:
    def skill2(self):
        print("Father is Gardening")

class Son(Father, Mother):
    def skill3(self):
        print("Son is Programming")

obj1 = Son()
obj1.skill1()
obj1.skill2()
obj1.skill3()