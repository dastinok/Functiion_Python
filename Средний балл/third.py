A = 90
B = 80
C = 70
D = 60



def deter_third(num_3):
    if num_3 >= A:
        b = f'{num_3} = A'
        print(b)
        return b
    elif B <= num_3 < A:
        b = f'{num_3} = B'
        print(b)
        return b
    elif C <= num_3 < B:
        b = f'{num_3} = C'
        print(b)
        return b
    elif D <= num_3 < C:
        b = f'{num_3} = D'
        print(b)
        return b
    else:
        b = f'{num_3} = F'
        print(b)
        return b