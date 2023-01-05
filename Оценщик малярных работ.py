

PAINT_CAPACITY = 5
SQUARE_METERS = 10
HOURS = 8
COST_HOUR = 2000


def main():
    print('Стоимость малярных работ')

    surface_area = float(input('Введите площадь поверхности стены: '))
    print(f'Площадь поверхности стены = {surface_area} кв.м.')
    price_paint_capacity = float(input('Введите цену 5-литровой емкости краски: '))
    print(f'Цена 5-литровой емкости краски = {price_paint_capacity} рублей')
    g = get_paint(surface_area)
    print('-------------------------------')
    print(f'Кол-во требуемых литров краски = {g: .2f}')
    print('-------------------------------')
    box_paint = g / PAINT_CAPACITY
    print(f'Количество требуемых емкостей = {box_paint: .2f} штук')
    print('-------------------------------')
    h = get_hours(surface_area)
    print(f'Количество рабочих часов = {h: .2f}')
    print('-------------------------------')
    cost_paint = price_paint_capacity * box_paint
    print(f'Стоимость краски = {cost_paint: .2f} рублей')
    print('-------------------------------')
    cost_work = h * COST_HOUR
    print(f'Стоимость работ = {cost_work:,.2f} рублей')
    print('-------------------------------')
    total_cost_of_painting_works = cost_work + cost_paint
    print(f'Общая стоимость малярных работ = {total_cost_of_painting_works: .2f} рублей')



def get_paint(surface_area):
    liters_of_paint = surface_area * PAINT_CAPACITY / SQUARE_METERS
    return liters_of_paint

def get_hours(surface_area):
    hours = surface_area * HOURS / SQUARE_METERS
    return hours






if __name__ == '__main__':
    main()