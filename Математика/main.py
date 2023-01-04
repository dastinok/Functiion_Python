import begin
import add
import sub
import div
import mult
import wrong

NO = 'Нет'

def main():

    begin.display_menu()

    choice = int(input('Строка ввода: '))

    num_1 = float(input('Первое число: '))
    num_2 = float(input('Второе число: '))


    if choice == begin.ADD:
        print('Вы выбрали сложение')
        total = add.add(num_1, num_2)
        print(f'Сумма = {total: .2f}')




    elif choice == begin.SUB:
        print('Вы выбрали вычитание')
        total = sub.sub(num_1, num_2)
        print(f'Разность = {total: .2f}')


    elif choice == begin.DIV:
        print('Вы выбрали деление')
        total = div.div(num_1, num_2)
        print(f'Деление = {total: .2f}')

    elif choice == begin.MULT:
        print('Вы выбрали умножение')
        total = mult.mult(num_1, num_2)
        print(f'Произведение = {total: .2f}')

    again = input('Вы хотите вернуться в меню? ENTER - вернуться или Нет? ')
    if again == 'Нет':
        print('Спасибо за работу')
    else:
        main()








main()