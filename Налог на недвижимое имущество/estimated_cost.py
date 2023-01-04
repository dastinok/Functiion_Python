
COEF = 0.6

def estimated_cost(num):
    cost = num * COEF
    print('-------------------------------------')
    print(f'Оценочное имущество = {cost:,.2f} баксов')
    return cost

