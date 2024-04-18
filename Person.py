class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.mobile = ""

    def set_values(self):
        self.name = input("enter name: ")
        self.age = int(input("enter age: "))
        self.mobile = input("enter mobile number: ")

    def print_values(self):
        print("name:", self.name)
        print("age:", self.age)
        print("mobile:", self.mobile)

# Creating an object of the Person class
person_obj = Person()

# Setting values for the person object
person_obj.set_values()

# Printing the values using class object
person_obj.print_values()
