
FEDERAL_TAX = 0.05
MUNIC_TAX = 0.025

def main():
    sales_volume = float(input('Общий объем продаж: '))
    sum_fed_tax = sales_volume * FEDERAL_TAX
    sum_mun_tax = sales_volume * MUNIC_TAX
    all_sum = sum_fed_tax + sum_mun_tax

    print(f'Сумма федерального налога = {sum_fed_tax:,.2f}\n'
          f'Сумма муниципального налога = {sum_mun_tax:,.2f}\n'
          f'Общий налог с продаж = {all_sum:,.2f}')






if __name__ == '__main__':
    main()

