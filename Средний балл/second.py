A = 90
B = 80
C = 70
D = 60



def deter_second(num_2):
    if num_2 >= A:
        b = f'{num_2} = A'
        print(b)
        return b
    elif B <= num_2 < A:
        b = f'{num_2} = B'
        print(b)
        return b
    elif C <= num_2 < B:
        b = f'{num_2} = C'
        print(b)
        return b
    elif D <= num_2 < C:
        b = f'{num_2} = D'
        print(b)
        return b
    else:
        b = f'{num_2} = F'
        print(b)
        return b