"""
This is module of my homework 11
"""
# Task 1. Create geometric progression generator

# *1* Геометрическая прогрессия: каждое следующее число возводит во 2ю степень


def generation_1(item: int):
    """
    This is function 1 for geometric progression generator
    """

    while item < 1500:
        item **= 2
        yield item


iter_obj_1 = generation_1(2)

print(list(generation_1(2)))  # Вывод списком
for i in iter_obj_1:
    print(i)

# *2* Геометрическая прогрессия: каждое следующее число умножается на 2


def generation_2(item: int, value: int):
    """
    This is function 2 for geometric progression generator
    """

    while True:
        yield item
        item *= value


iter_obj_2 = generation_2(5, 2)

for i in iter_obj_2:
    print(i)
    if i > 100:
        break




