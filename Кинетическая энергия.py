
COEF_1 = 1 / 2
COEF_2 = 2

def main():
    weight = float(input('Введите массу тела в кг: '))
    speed = float(input('Введите скорость тела в м/с: '))

    k = get_kinetic_energy(weight, speed)
    print(f'Кинетическая энергия = {k:,.2f}')

def get_kinetic_energy(w, s):
    kinetic_energy = COEF_1 * w * s ** COEF_2
    return kinetic_energy





if __name__ == '__main__':
    main()