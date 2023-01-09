A = 90
B = 80
C = 70
D = 60



def deter_fourth(num_4):
    if num_4 >= A:
        b = f'{num_4} = A'
        print(b)
        return b
    elif B <= num_4 < A:
        b = f'{num_4} = B'
        print(b)
        return b
    elif C <= num_4 < B:
        b = f'{num_4} = C'
        print(b)
        return b
    elif D <= num_4 < C:
        b = f'{num_4} = D'
        print(b)
        return b
    else:
        b = f'{num_4} = F'
        print(b)
        return b