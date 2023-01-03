

COEF = 0.6214

def main():
    km = float(input('Введите расстояние в километрах: '))


    mile = km * COEF
    print(f'Мили = {mile: .2f}')



main()