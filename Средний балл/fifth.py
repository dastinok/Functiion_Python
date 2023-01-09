A = 90
B = 80
C = 70
D = 60



def deter_fifth(num_5):
    if num_5 >= A:
        b = f'{num_5} = A'
        print(b)
        return b
    elif B <= num_5 < A:
        b = f'{num_5} = B'
        print(b)
        return b
    elif C <= num_5 < B:
        b = f'{num_5} = C'
        print(b)
        return b
    elif D <= num_5 < C:
        b = f'{num_5} = D'
        print(b)
        return b
    else:
        b = f'{num_5} = F'
        print(b)
        return b