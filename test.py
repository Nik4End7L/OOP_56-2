# def calculator(num1: float, operator: str, num2: float) -> float:
#     """ Простой Калькулятор созданный одной функцией, принмиает число_1, после арифм.оператор, и число_2. """

#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             raise ZeroDivisionError("Делить на ноль нельзя.")
#         return num1 / num2
#     elif operator == '//':
#         if num2 == 0:
#             raise ZeroDivisionError("Делить на ноль нельзя.")
#         return num1 // num2
#     elif operator == '%':
#         if num2 == 0:
#             raise ZeroDivisionError("Делить на ноль нельзя.")
#         return num1 % num2
#     elif operator == '**':
#         return num1 ** num2
#     else:
#         raise ValueError("Неподдерживаемый арифметический оператор. Используйте +, -, *, /, //, %, **")

# print(calculator(4, '+', 7))
# print(calculator(4, '-', 7))
# print(calculator(4, '*', 7))
# print(calculator(14, '/', 7))
# print(calculator(4, '//', 7))
# print(calculator(4, '%', 7))
# print(calculator(4, '**', 7))
