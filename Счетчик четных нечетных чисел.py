import random

BEGIN = 1
MAX = 100

START = 1
END = 1000


def main():
    for x in range(BEGIN, MAX):
        numbers = random.randrange(START, END)
        if numbers % 2 == 0:
            print(f'{x}) {numbers} - четное')
        else:
            print(f'{x}) {numbers} - нечетное')


if __name__ == '__main__':
    main()