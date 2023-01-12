

def main():



    def is_prime(r):
        status = True
        t = 0
        for x in range(r-2):
            t = t + 1
            num = r % (r-t)
            if num == 0:
                status = True
            else:
                status = False
        return status




    number = int(input('Введите целое число: '))
    if is_prime(number):
        print(f'Одно число поделилось без остатка отличное от 1 и {number} следовательно:')
        print('Число не простое')
    else:
        print(f'Ни одно число не поделилось без остатка отличное от 1 и {number} следовательно:')
        print('Число простое')





if __name__ == '__main__':
    main()