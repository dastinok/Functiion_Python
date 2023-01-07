


def main():
    a = enter_num_1()
    b = enter_num_2()


    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print('Они РАВНЫ')
        main()






def enter_num_1():
    res = int(input('Введите 1 значение: '))
    return res

def enter_num_2():
    res = int(input('Введите 2 значение: '))
    return res














if __name__ == '__main__':
    main()