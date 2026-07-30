class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

obj = Dog()
obj.sound()
obj.bark()


