from typing import Sequence, Optional

def calculate_total_delivery_cost(
    product_name: str,
    weights: Sequence[int | float],
    prices: Sequence[int | float],
    discount: Optional[int | float] = None,
    currency_rate: int | float = 1,
    *extra_costs: float
) -> dict[str, float]:
    """
    Вычисляет общую стоимость доставки с учетом веса, цены, скидки и доп. расходов.

    product_name: Название товара.
    weights: Коллекция с весами партий (list или tuple).
    prices: Коллекция с ценами за кг (list или tuple).
    discount: Скидка в денежном эквиваленте (если есть).
    currency_rate: Коэффициент пересчета валюты (по умолчанию 1).
    extra_costs: Произвольное количество дополнительных расходов.
    return Итоговая стоимость в целевой валюте.
    """

    is_equal: bool = len(weights) == len(prices)
    if is_equal:
        total_sum : float = 0
        for i in range(len(weights)):
            position_cost: float = weights[i] * prices[i]
            total_sum += position_cost

        if discount is not None:
            total_sum *= (1 - discount)

        for cost in extra_costs:
            total_sum += cost
        
        total_sum *= currency_rate

        return {product_name: total_sum}
    else:
        print('Не равное количество')
        return {}


result = calculate_total_delivery_cost("Овощная партия", [100, 50], [4, 6], 0.1, 1, 20, 15)
for key, value in result.items():
    print(f'Товар: {key}, итоговая стоимость: {value}')

result = calculate_total_delivery_cost("Фруктовая партия", (30, 20, 10), (15, 12, 18), None, 1.2, 25)
for key, value in result.items():
    print(f'Товар: {key}, итоговая стоимость: {value}')