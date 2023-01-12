def main():



    def is_prime(num):
        status = True
        if num == 2:
            status = False

        num_2 = 1
        for counter in range(num-2):
            num_2 = num_2 + 1
            remain = num % num_2
            if remain == 0:
                status = True
                break

            else:
                status = False
                pass
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