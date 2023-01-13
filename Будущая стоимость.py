

def main():
    amount_acc = float(input('Введите сумму на счете (в рублях): '))
    int_rate = float(input('Введите ежемесячную процентную ставку (в процентах): '))
    num_month = float(input('Введите кол-во месяцев: '))

    get_money(amount_acc, int_rate, num_month)

def get_money(a, i, n):
        x = i / 100


        future_amount = a * (1 + x) ** n
        print(f'{future_amount:,.2f} рублей')




if __name__ == "__main__":
    main()