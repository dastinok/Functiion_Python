
PERCENT = 0.8


def main():
    cost_build = float(input('Какова стоимость строения (в рублях): '))
    print(f'Стоимость строения равна {cost_build} рублей')

    min_ins_amount = cost_build * PERCENT
    print(f'Минимальная страховая сумма = {min_ins_amount}')





if __name__ == '__main__':
    main()