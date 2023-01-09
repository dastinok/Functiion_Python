
A = 90
B = 80
C = 70
D = 60



def deter_first(num_1):
    if num_1 >= A:
        b = f'{num_1} = A'
        print(b)
        return b
    elif B <= num_1 < A:
        b = f'{num_1} = B'
        print(b)
        return b
    elif C <= num_1 < B:
        b = f'{num_1} = C'
        print(b)
        return b
    elif D <= num_1 < C:
        b = f'{num_1} = D'
        print(b)
        return b
    else:
        b = f'{num_1} = F'
        print(b)
        return b
