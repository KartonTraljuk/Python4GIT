`""" This module completes homework of the 5 lesson """
# TODO:

# Task 1.

# my_string = b'r\xc3\xa9sum\xc3\xa9'
# print(my_string)
# my_string_utf8 = my_string.decode('utf-8')
# print(my_string_utf8)
# my_string_latin1 = my_string_utf8.encode('latin-1')
# print(my_string_latin1)
# my_result_string = my_string_latin1.decode("latin-1")
# print(my_result_string)

# ---------------------------------------------------------------------------
# Task 2.

# str_1 = input(f'you 1st string is: ')
# str_2 = input(f'you 2nd string is: ')
# str_3 = input(f'you 3rd string is: ')
# str_4 = input(f'you 4th string is: ')
# print(f"{str_1}\n{str_2}\n{str_3}\n{str_4}\n")
#
# file = open('text.txt', 'w')
# file.write(f"{str_1}\n{str_2}")
# file.close()
#
# file = open('text.txt', 'r')
# print(file.read(),'\n')
#
# file = open('text.txt', 'a')
# file.write(f"\n{str_3}\n{str_4}")
# file.close()
#
# file = open('text.txt', 'r')
# print(file.read())
# --------------------------------------------------------------------------

# Task 3

# import json
#
# dict_1 = {
#     111111: ('Janna', 35),
#     222222: ('Pasha', 21),
#     333333: ('Lena', 17),
#     444444: ('Dima', 26),
#     555555: ('Grisha', 72)
# }
# print(dict_1)
#
# with open('less_6.json', 'w') as file:
#     json.dump(dict_1, file)


# --------------------------------------------------------------------------

# Task 4. Не выполняется - я устал добиваться правды)

import json
import csv

with open('less_6.json', 'r') as file:
    dict_1 = json.load(file)
    print(dict_1)

list_dict_1 = []
dict_person = {}

for key, value in dict_1.items():
    dict_person['id'] = key
    dict_person['name'] = value[0]
    dict_person['age'] = value[1]

    list_dict_1.append(dict_person)

dict_1 = list_dict_1

col = ['id', 'name', 'age']
with open('less_6.csv', 'w') as file:
    wr = csv.DictWriter(file, fieldnames=dict_1[0].keys())
    wr.writeheader()
    wr.writerow(dict_1)

# with open('less_6.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(col)
#
# with open('less_6.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerows(dict_1)

