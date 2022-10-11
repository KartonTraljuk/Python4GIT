"""
This module completes homework of the 8 lesson
"""
import time

# Task 1-2.

class Auto:
    """
    This is parental class Auto
    """
    brand = ""
    age = 0
    color = ""
    mark = ""
    weight = 0

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        age += 1

class Truck(Auto):
    """
    This is child class Truck from parental class Auto
    """
    max_load = 0

    def move(self):
        print('attention')
        return super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)



class Car(Auto):
    """
    This is child class Car from parental class Auto
    """
    max_speed = input('Input max speed: ')

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')

auto = Auto()
auto.move()
truck = Truck()
truck.move()
truck.load()
car = Car()
car.move()








