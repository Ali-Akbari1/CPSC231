# Ali Akbari 30171539

# Car class
class Car:

    # This is my constructor which takes in 5 parameters
    # self, yr, brand, typ, and clr, miles
    def __init__(self, yr, brand, typ, clr, miles=0):

        # These are the attributes or fields of my class
        self.year = yr  # year is an attribute/field
        self.make = brand  # make is an attribute/field
        self.model = typ  # model is an attribute/field
        self.colour = clr  # colour is an attribute/field
        self.mileage = miles  # mileage is an attribute/field

    # This is my method carInfo which prints the car info of the user
    def carInfo(self):
        print("Your car is a", self.year, self.make, self.model, "with the colour", self.colour,
              "and has driven", self.mileage, "kilometres")

    # This is another method called setMileage which sets the mileage of the car
    def setMileage(self, mileage):
        self.mileage = mileage


# The name of the object is car of the Car class,
# We then call the methods setMileage and carInfo
car = Car(2022, "Honda", "Civic", "Red")
car.setMileage(500)
car.carInfo()

