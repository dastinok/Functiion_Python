
BEGIN = 0
END = 10
STEP = 1
G = 9.8
COEF = 1 / 2


def main():
    print('-----Время падения под силой тяжести------')
    time = int(input('Введите время в сек: '))
    falling_distance(time)




def falling_distance(TIME):
    #TIME = int(input('Введите время в сек: '))
    for i in range(BEGIN, END, STEP):
        s = COEF * G * TIME ** 2
        TIME += 1
        print(f'{s:,.2f} метров - {TIME - 1} секунд(у)')





if __name__ == '__main__':
    main()