"""
This module completes homework of the 8 lesson
"""
import time

# Task 1-2.

class Auto:
    """
    This is parental class Auto
    """

    def __init__(self,
        brand: str,
        age: int,
        color: str,
        mark: str,
        weight: int
    ):  # initializing class Auto attributes


        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        return self.age


class Truck(Auto):
    """
    This is child class Truck from parental class Auto
    """
    def __init__(self,
        brand: str,
        age: int,
        color: str,
        mark: str,
        weight: int,
        max_load: int
    ):  # initializing parent attributes and adding an attribute 'max_load'


        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
        self.max_load = max_load


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

    def __init__(self,
        brand: str,
        age: int,
        color: str,
        mark: str,
        weight: int,
        max_speed: int
    ):    # initializing parent attributes and adding an attribute 'max_speed'

        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
        self.max_speed = max_speed


    def move(self):
        super().move()
        print(f'max speed is {self.max_speed} km/h')



# Truck "MAN"
truck_1 = Truck('MAN', 2020, 'RED', 'Chacago-70', 5200, 15_000)
print(f'===================== I M  TRUCK !!!! =========================')
print(
    f'Brand: {truck_1.brand}\n'
    f'Year of release: {str(truck_1.age)}\n'
    f'Color: {truck_1.color}\n' 
    f'Mark: {truck_1.mark}\n'
    f'Weight: {str(truck_1.weight)}\n'
    f'Max. load: {str(truck_1.max_load)}'
)
print(f'Yahoo! Birthday! {truck_1.birthday()}', sep='')

truck_1.load()
truck_1.move()
truck_1.stop()


# Truck "VOLVO"
truck_2 = Truck('VOLVO', 2018, 'YELLOW', 'D904-PICASSO', 6400, 22_000)
print(f'===================== I M  TRUCK !!!! =========================')
print(
    f'Brand: {truck_2.brand}\n'
    f'Year of release: {str(truck_2.age)}\n'
    f'Color: {truck_2.color}\n' 
    f'Mark: {truck_2.mark}\n'
    f'Weight: {str(truck_2.weight)}\n'
    f'Max. load: {str(truck_2.max_load)}'
)

print(f'Yahoo! Birthday! {truck_2.birthday()}', sep='')

truck_2.load()
truck_2.move()
truck_2.stop()


# Car "Renault"
car_1 = Car('Renault', 2002, 'BLUE', 'VelSatis', 2300, 220)
print(f'===================== I M  CAR !!!! =========================')
print(
    f'Brand: {car_1.brand}\n'
    f'Year of release: {str(car_1.age)}\n'
    f'Color: {car_1.color}\n' 
    f'Mark: {car_1.mark}\n'
    f'Weight: {str(car_1.weight)}\n'
    f'Max. speed: {str(car_1.max_speed)}'
)
print(f'Yahoo! Birthday! {car_1.birthday()}', sep='')

car_1.move()
car_1.stop()


# Car "Renault"
car_2 = Car('BMW', 1998, 'BLACK', '530', 2100, 235)
print(f'===================== I M  CAR !!!! =========================')
print(
    f'Brand: {car_2.brand}\n'
    f'Year of release: {str(car_2.age)}\n'
    f'Color: {car_2.color}\n' 
    f'Mark: {car_2.mark}\n'
    f'Weight: {str(car_2.weight)}\n'
    f'Max. speed: {str(car_2.max_speed)}'
)
print(f'Yahoo! Birthday! {car_2.birthday()}', sep='')

car_2.move()
car_2.stop()


