# oops concept
class Car:
    wheels = 4
    make=""
    year=""
    model= ""

    def display_info(self):
        print(f'Car info:  \nyear of manufacturing : {self.year} \nMaker : {self.make} \nModel Name : {self.model} \nWheels in car :{self.wheels}')

car1= Car()
car2= Car()
car1.model= "S-Class"
car1.make= "Mercedes"
car1.year= "2024"

car2.model= "Q7"
car2.make= "Audi"
car2.year= "2024"
car1.display_info()
car2.display_info()



