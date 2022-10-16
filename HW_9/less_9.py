"""
This is my homework 9
"""
from dataclasses import dataclass
from abc import ABC

# Task 1. Creat the @dataclass

# @dataclass
# class Film(ABC):
#     """
#     This is @dataclass of my film
#     """
#
#     name: str
#     director: str
#     main_character: str
#     duration_min: int
#
# class AnimationFilm():
#     """
#     This is class of my animation film
#     """
#
#     def __init__(self, film):
#         self.film = film
#
#     def show_film(self):
#         print(
#             f'Animation film "{self.film.name}"! '
#             f'Director is {self.film.director}! '
#             f'Main character is {self.film.main_character}! '
#             f'Duration of this film is {self.film.duration_min} minutes!'
#         )
#
#
# film_1 = Film(
#     name='Cat',
#     director='Tedd Jonson',
#     main_character='Alise Cooper',
#     duration_min=120
# )
#
# film_2 = Film(
#     name='Dog',
#     director='Mers Bretson',
#     main_character='Candy Joocer',
#     duration_min=90
# )
#
# af_1 = AnimationFilm(film_1)
# af_1.show_film()
#
# af_2 = AnimationFilm(film_2)
# af_2.show_film()

# ----------------------------------------------------------------------------
# Task 2. Create @staticmethod in my class

# class MyFilm:
#     """
#     This is class for keep information about film
#     """
#
#     book = 'Snow'
#     film = 'Horror'
#     dur_min = 97
#
#     @staticmethod
#     def my_method_1():
#         print(
#         f'This is {MyFilm.film} film '
#         f'for famous book "{MyFilm.book}" '
#         f'and duration of  {MyFilm.dur_min} minutes!'
#     )
#
# # # вызов можно осуществлять без создания экземпляра класса
# MyFilm.my_method_1()
#
# # НО! вызвать можно и через создание экземпляра класса
# mf = MyFilm()
# mf.my_method_1()

# ----------------------------------------------------------------------------

# Task 3. Create @classmethod in my class
#
# class MyClass:
#     book = 'Snow'
#     film = 'Horror'
#     dur_min = 97
#
#     @classmethod
#     def my_method_2(slc):
#         print(
#         f'This is {MyClass.film} film '
#         f'for famous book "{MyClass.book}" '
#         f'and duration of {MyClass.dur_min} minutes!'
#     )
#
# # вызов можно осуществлять без создания экземпляра класса
# MyClass.my_method_2()
#
# # НО! вызвать можно и через создание экземпляра класса
# mc = MyClass()
# mc.my_method_2()

# ---------------------------------------------------------------------------
# Task 4*. Create metaclass

# class MyClass(metaclass=type):
#     ...
#
#
# mc = MyClass()
# print(mc.__class__())








