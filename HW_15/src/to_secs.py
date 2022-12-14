"""Этот модуль конвертирует Фаренгейты в Кельвины
"""
from prettytable import PrettyTable


def secs(minutes: int) -> str:
    """
    Конвертирует температуре из градусов по Фаренгейту в градусы Кльвина.
    @param fahrenheit: значение в градусах по Фаренгейти
    :return: текстовая таблица со значениями в Фаренгейтах и Кельвинах

    ```
        +-------------+------------+
        | МинутахНАХ  | СекундаНАХ |
        +-------------+------------+
        |      1      |     60     |
        +-------------+------------+
    ```
    """

    sec_value = minutes * 60

    table = PrettyTable(['МинутахНАХ ', 'СекундаНАХ'])
    table.add_row([minutes, sec_value])

    return table.get_string()

