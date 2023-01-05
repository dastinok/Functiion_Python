
COEF_FAT = 9
COEF_CARB = 4


def main():
    print('Программа расчета жиров и углеводов')
    print('')

    gram_fat = float(input('Введите сколько жиров употребили в граммах: '))
    gram_carb = float(input('Введите сколько углеводов употребили в граммах: '))

    calorie_fat = gram_fat * COEF_FAT
    calorie_carb = gram_carb * COEF_CARB

    print(f'Калории от жиров = {calorie_fat} граммов')
    print(f'Калории от углеводов = {calorie_carb} грамм')




if __name__ == '__main__':
    main()