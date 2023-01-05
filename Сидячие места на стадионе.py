
A = 20
B = 15
C = 10


def main():


    place_A = int(input('Введите сколько мест класса A: '))
    place_B = int(input('Введите сколько мест класса B: '))
    place_C = int(input('Введите сколько мест класса C: '))

    a = place_A * A
    b = place_B * B
    c = place_C * C

    print(f'Класс A = {a} баксов\n'
          f'Класс B = {b} баксов\n'
          f'Класс С = {c} баксов\n'
          f'Сумма = {a + b + c} баксов')







if __name__ == '__main__':
    main()