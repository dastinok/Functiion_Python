



def main():
    first_age = int(input('Введите свой возраст: '))
    second_age = int(input('Введите возраст друга/подруги: '))
    total = amount(first_age, second_age)
    print(f'Возраст участников = {total} лет')


def amount(num_1, num_2):
    total = num_1 + num_2
    return total



main()
