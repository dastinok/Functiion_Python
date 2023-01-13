import random





a = 1
b = 1000

def main():
    number = random.randrange(1, 100)
    print('Компьютер загадал число')
    print(number)

    get_human_num(number)


def get_human_num(value):
    for x in range(a, b):

        human_num = int(input('Введите число которое загадал комп: '))
        if human_num == value:
            print('УРА! Вы победили')
            print(f'Число компа - {value}. Ваше число - {human_num} - {x} попытка')
            break
        elif human_num > value:
            print(f'Ваше число больше, чем у компа. - {x} попытка')

        else:
            print(f'Ваше число меньше, чем у компа. - {x} попытка')






if __name__ == "__main__":
    main()
    while True:
        flag = input('Ещё раз? [да/нет]: ')
        if flag == 'да':
            main()
        else:
            break