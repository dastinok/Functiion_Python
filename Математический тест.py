import random



def main():
    print('--------Математический тест--------')
    number_1 = random.randint(0, 999)
    number_2 = random.randint(0, 999)
    print(f'\t  {number_1}\n'
          f'\t+ {number_2}')
    answer = int(input('Введите ваш ответ: '))

    add = get_add(number_1, number_2)


    if answer == add:
        print('УРА! Вы посчитали верно!')
        again = input('Вернуться в меню - Enter. Выйти - Exit ')
        if again == 'Exit':
            print('Спасибо за работу')
        else:
            main()
    else:
        print('Ответ неверный!')
        again = input('Вы хотите вернуться в меню? ENTER - вернуться или Нет? ')
        if again == 'Нет':
            print('Спасибо за работу')
        else:
            main()


def get_add(num_1, num_2):
    total = num_1 + num_2
    return total









if __name__ == '__main__':
    main()