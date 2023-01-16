import random





def main():
    num_comp = random.randrange(1, 4)


    choice = get_menu()
    print(f'Выбор игрока: {choice}')
    print('************************')

    if num_comp == 1:
        print('Выбор Компьютера - Камень')
        print('************************')
    elif num_comp == 2:
        print('Выбор Компьютера - Ножницы')
        print('************************')
    else:
        print('Выбор Компьютера - Бумага')
        print('************************')

    if choice == 'Камень' and num_comp == 1:
        print('Раунд не выявил победителей')
        main()
    elif choice == 'Ножницы' and num_comp == 2:
        print('Раунд не выявил победителей')
        main()
    elif choice == 'Бумага' and num_comp == 3:
        print('Раунд не выявил победителей')
        main()
    elif choice == 'Камень' and num_comp == 2:
        print(f'Победил {choice}. Вы Выйграли. УРА!!!')
    elif choice == 'Камень' and num_comp == 3:
        print(f'Победил Бумага. Компьютер выйграл((')
    elif choice == 'Ножницы' and num_comp == 1:
        print(f'Победил Камень. Компьютер выйграл((')
    elif choice == 'Ножницы' and num_comp == 3:
        print(f'Победил {choice}. Вы Выйграли. УРА!!!')
    elif choice == 'Бумага' and num_comp == 1:
        print(f'Победил {choice}. Вы Выйграли. УРА!!!')
    elif choice == 'Бумага' and num_comp == 2:
        print(f'Победил Ножницы. Компьютер выйграл((')
    else:
        print('123')





def get_menu():
    print('Меню выбора:\n'
          'Камень\tНожницы\tБумага')
    num_hum = (input('Строка ввода выбора: '))
    if num_hum == 'Камень':
        print('Игрок сделал выбор')
        print('************************')
    elif num_hum == 'Ножницы':
        print('Игрок сделал выбор')
        print('************************')
    elif num_hum == 'Бумага':
        print('Игрок сделал выбор')
        print('************************')
    else:
        print('Не то ввели')
    return num_hum












if __name__ == '__main__':
    main()