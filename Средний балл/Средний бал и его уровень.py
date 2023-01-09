import first
import second
import third
import fourh
import fifth

def main():



    first_score = float(input('Введите оценку: '))
    f = first.deter_first(first_score)
    second_score = float(input('Введите первую оценку: '))
    s = second.deter_second(second_score)
    third_score = float(input('Введите третью оценку: '))
    t = third.deter_third(third_score)
    fourth_score = float(input('Введите четвертую оценку: '))
    fo = fourh.deter_fourth(fourth_score)
    fifth_score = float(input('Введите пятую оценку: '))
    fi = fifth.deter_fifth(fifth_score)

    print('*************')
    print(f'{f}\n'
          f'{s}\n'
          f'{t}\n'
          f'{fo}\n'
          f'{fi}\n')

    calc_average(first_score, second_score, third_score, fourth_score, fifth_score)

def calc_average(num_1, num_2, num_3, num_4, num_5):
    average = (num_1 + num_2 + num_3 + num_4 + num_5) / 5
    print(f'Средний бал = {average}')

    while True:
        flag = input('Ещё раз? [да/нет]: ')

        if flag == 'да':
            main()
        else:
            break



if __name__ == '__main__':
    main()

