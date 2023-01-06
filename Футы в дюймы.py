
COEF = 12

def main():
    number_of_feet = float(input('Введите кол-во футов: '))
    f = feet_to_inches(number_of_feet)
    print(f'Кол-во дюймов = {f:,.2f}')



def feet_to_inches(num_feet):
    trans = num_feet * COEF
    return trans








if __name__ == '__main__':
    main()