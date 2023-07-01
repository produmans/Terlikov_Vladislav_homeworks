"""
1)	Реализовать калькулятор с 4 методами:
Сумма, вычитание , умножение, деление.
Метод принимает 2 аргумента и возвращает результат.
Невалидные данные должны быть обработаны.
Валидатором является в программе метод, который будет проверять ваши аргументы на то, является ли это число
"""


class Calculate:
    def validator(self, num1, num2):
        try:
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                return True
        except ValueError:
            return False

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return '"Ошибка: на ноль делить нельзя"'


calculate = Calculate()
while True:
    select_operation = ("0: Выход из программы \n"
                        "1: Сложение\n"
                        "2: Вычитание\n"
                        "3: Умножение\n"
                        "4: Деление")
    print(select_operation)
    enter_operation = int(input('Введите номер операции: '))
    if enter_operation == 0:
        print('Вы вышли из программы')
        break

    num1 = 5
    # num2 = 23
    num2 = '23'
    if calculate.validator(num1, num2):
        if enter_operation == 1:
            print(f'{num1} + {num2} = {calculate.addition(num1, num2)}')
        elif enter_operation == 2:
            print(f'{num1} - {num2} = {calculate.subtraction(num1, num2)}')
        elif enter_operation == 3:
            print(f'{num1} * {num2} = {calculate.multiplication(num1, num2)}')
        elif enter_operation == 4:
            print(f'{num1} / {num2} = {calculate.division(num1, num2)}')
    else:
        print('"Ошибка: значение не является числом!"')
