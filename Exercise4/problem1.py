# Ali Akbari 30171539

# Car class
class Car:

    # This is my constructor which takes in 5 parameters
    # self, yr, brand, typ, and clr
    def __init__(self, yr, brand, typ, clr):

        # These are the attributes or fields of my class
        numOfTires = 4 # numOfTires is a field of the class Car
        self.year = yr  # year is my attribute/field
        self.make = brand  # make is my attribute/field
        self.model = typ  # model is my attribute/field
        self.colour = clr  # colour is my attribute/field

    # This is my method carInfo which prints the car info of the user
    def carInfo(self):
        print("Your car is a", self.year, self.make, self.model, "with the colour", self.colour)


# The name of the object is car of the Car class, and we then call the method carInfo()
car = Car(2022, "Honda", "Civic", "Red")
car.carInfo()


