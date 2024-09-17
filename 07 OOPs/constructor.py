# Constructor
class Car:
    wheels = 4
    make="porshe"
    year=""
    model= ""
    def __init__(self,make1,model1,year1):
        self.make= make1
        self.model =model1
        self.year = year1

    def display_info(self):
        print(f'Car info:  \nyear of manufacturing : {self.year} \nMaker : {self.make} \nModel Name : {self.model} \nWheels in car :{self.wheels}')
car3 = Car("Toyota","2023","Fortuner Legender")
car3.display_info()
print(Car.make)