def calculate_purchase(product_name: str, weight: int, price: float) -> tuple[str, float]:
    """
    product_name - название товара
    weight - вес партии
    price - цена за кг
    """

    try:
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight

        return product_name, total_cost
    except TypeError as e:
        print(type(e))
        print('Ошибка: В расчет попал неподходящий тип вместо числа')
    except ValueError as e:
        print(type(e))
        print('Ошибка: В float() передали текст, который нельзя превратить в число')
    except ZeroDivisionError as e:
        print(type(e))
        print('Ошибка: Произошло деление на 0')
    finally:
        print('--- Проверка партии завершена ---')
    

calculate_purchase('Томаты', 100, 2.5)
calculate_purchase('Огурцы', 'пятьдесят', 1.8)
calculate_purchase('Перец', 0, 4)
calculate_purchase('Зелень', [10], 5)

    