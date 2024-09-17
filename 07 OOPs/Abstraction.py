#Abstraction Assignment 3

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def name(self):
        pass
    def start(self):
        pass
    def stop(self):
        pass
class Bike(Vehicle):
    def name(self):
        return "Bike"
    def start(self):
        return "By Kick..."
    def stop(self):
        return "by kill switch"
class Car(Vehicle):
    def name(self):
        return "car"
    def start(self):
        return "by Switch..."
    def stop(self):
        return "by key"
class Bus(Vehicle):
    def name(self):
        return "bus"

    def start(self):
        return "By dhakkka..."
    def stop(self):
        return "By mood..."
class Garage(Vehicle):
    vehicle_List= []
    def add_vehicle(vehicle:Vehicle):
        Garage.vehicle_List.append(vehicle.name())
    def garageMethod(vehicle : Vehicle):
        print(f"To start vehile {vehicle.start()} and to stop it {vehicle.stop()}")

bike = Bike()
car = Car()
bus = Bus()

print(bike.start())
print(bike.stop())

print(car.start())
print(car.stop())

print(bus.start())
print(bus.stop())

Garage.garageMethod(bike)
Garage.add_vehicle(bike)
Garage.garageMethod(car)
Garage.add_vehicle(car)
Garage.garageMethod(bus)
Garage.add_vehicle(bus)
print(Garage.vehicle_List)