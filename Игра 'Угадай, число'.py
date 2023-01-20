import random # Импортируем модуль для генерации случайных чисел

A = 1
B = 21

effort = 0  # Переменная для хранения попыток игрока


name_gamer = input('Как вас зовут: ')

num = random.randint(A, B) # Генерерируем случайное число от и до. Число загад компом

print(f'Компьютер загадал число от {A} до {B-1} ')

for effort in range(6):
    print('Начинай угадывать))')
    guess = int(input('Введите число: '))

    if guess < num:
        print('Ваше число меньше загаданного')

    if guess > num:
        print('Ваше число больше загаданного')

    if guess == num:
        break

# Когда попытки закончились переходим к нижнему условию:

if guess == num:
    effort = str(effort + 1)
    print(f'Отлично {name_gamer}! Вы победили! УРА!')

if guess != num:
    num = str(num)
    print(f'Увы. Загаданное число было {num}')