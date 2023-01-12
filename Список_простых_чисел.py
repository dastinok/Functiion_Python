
BEGIN = 1
MAX = 101


def main():
    def is_prime(num):
        status = True
        if num == 2:
            status = False
        num_2 = 1
        for counter in range(num - 2):
            num_2 = num_2 + 1
            remain = num % num_2
            if remain == 0:
                status = True
                break
            else:
                status = False
                pass
        return status

    for i in range(BEGIN, MAX):
        if is_prime(i):
            pass
        else:
            print(f'число {i}: число простое')


if __name__ == '__main__':
    main()