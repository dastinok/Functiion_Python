

res = [(k, int(input(f'Введите сколько мест класса {k}: ')) * v) for k, v in {'A': 20, 'B': 15, 'C': 10}.items()]
print('\n'.join([f'Класс {i[0]} = {i[1]} баксов' for i in res]))