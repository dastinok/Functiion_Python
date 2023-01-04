


def main():
    startup()
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    function = input('Выберите действия: "+", "-" или "/": ')

    if function == "+":
        print('Вы выбрали сложение')
        total = add(first=num_1, second=num_2)
        print(total)
    elif function == "-":
        print('Вы выбрали вычитание')
        sub(first=num_1, second=num_2)
    elif function == "/":
        print('Вы выбрали деление')
        div(first=num_1, second=num_2)
    else:
        print('Вы выбрали не то')


def startup():
    print('Вас приветствует модуль "Математика"')




def add(first, second):
    result = first + second
    return result

def sub(first, second):
    result = first - second
    print(f'Разность = {result}')

def div(first, second):
    result = first / second
    print(f'Деление = {result: .2f}')


main()