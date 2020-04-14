'''
Calcultor v. 0.4
'''

def input_number():
    num = input("Введите число: ")
    if num == '':
        return None
    # просто попробуй
    try:
        # преобразовать переменную num в флоат
        num = float(num)
    # если вышла ошибка
    except ValueError:
        # можно вернуть как есть
        num = num
    return num

def input_oper():
    oper = input("Операция(*, /, +, -, ^): ")

    if oper == '':
        oper = None

    return oper

def calc_me(x=None,y=None, oper=None):
    # если x не присвоили значение - возвращаем ошибку
    if x is None:
        return "ERROR: send me Number1"
    # если y не присвоили значение - возвращаем ошибку
    if y is None:
        return "ERROR: send me Number1"
    # если x или y  не входит в типы int, float - возвращаем ошибку
    if (not isinstance(x, (int, float))) or (not isinstance(y, (int, float))):
        return "ERROR: now it is does not supported"

    if oper == '*':
        return x * y
    elif oper == '/':
        # если делитель == 0 то возвращаем ошибку
        if y == 0:
            return "ERROR: Divide by zero!"
        else:
            return x / y
    elif oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '^' or oper == '**':
        return x ** y
    else:
        return "ERROR: Uknow operation"

def body():
    # результат работы функции input_number запишется в переменную number1
    number1 = input_number()
    # результат работы функции input_oper запишется в переменную oper
    oper = input_oper()
    # результат работы функции input_number запишется в переменную number2
    number2 = input_number()
    # вызываем функцию calc_me с переменными которые мы ранее получили 
    # результат запишем в переменную result
    result = calc_me(number1,number2, oper)
    # выводим результат для пользователя
    print(result)

# это специальное служебное условие Питон
if __name__ == '__main__':
    # оно говорит, что если мы вызвали этот файл в консоли 
    # то надо выполнить функцию body
    body()