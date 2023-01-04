

FEDERAL_TAX = 0.05
REGION_TAX = 0.025

def main():
    sum_purchase = float(input('Сумма покупки равна: '))
    print(f'Вы купили товара на {sum_purchase} рублей')
    nalog1 = fed_tax(sum_purchase)
    nalog2 = reg_tax(sum_purchase)

    total_amount = sum_purchase + nalog1 + nalog2
    print(f'Сумма покупки с налогами = {total_amount} рублей ')

def fed_tax(summ):
    federal_tax_purchase = summ * FEDERAL_TAX
    print(f'Федеральный налог с покупки = {federal_tax_purchase} рублей')
    return federal_tax_purchase

def reg_tax(summ):
    region_tax_purchase = summ * REGION_TAX
    print(f'Региональный налог с покупки = {region_tax_purchase} рублей')
    return region_tax_purchase




if __name__ == '__main__':
    main()

