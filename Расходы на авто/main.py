import loan_payment
import insurance
import petrol
import engine_oil
import tires
import main_cost

YEAR = 12


def main():
    print('Добро пожаловать в программу "Расходы на авто"')
    l = loan_payment.loan_payment()
    i = insurance.insurance()
    p = petrol.petrol()
    e = engine_oil.engine_oil()
    t = tires.tires()
    m = main_cost.main_cost()

    monthly_expenses = l + i + p + e + t + m
    print(f'Месячные расходы на авто = {monthly_expenses:,.2f} рублей')

    year_expenses = monthly_expenses * YEAR
    print(f'Годовые расходы на авто = {year_expenses:,.2f} рублей')





if __name__ == '__main__':
    main()

