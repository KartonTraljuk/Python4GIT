# MyError собственный класс исключений
class MyError(Exception):
    """
    Это класс ошибок для проверки корректного ввода операции
    """


while True:


    oper = input(
        f'Input your operation:\n'
        f' "+"  для сложения;\n'
        f' "-"  для вычитания;\n'
        f' "*"  для умножение;\n'
        f' "/"  для деления.\n'
        f' or "q" for exit programm\n'
        f'Your operation is: '
    )


    try:
        if oper == 'q':
            print(f'Buy-buy!')
            break
        elif oper != '+' and oper != '-' and oper != '*' and oper != '/':
            print(oper)
            raise MyError(f'Invalid type operation!')
    except MyError as me:
        print(me)

    else:
        print(f'Your operation is: "{oper}"')
        break


    def get_operation(self) -> str:
        return self.oper












