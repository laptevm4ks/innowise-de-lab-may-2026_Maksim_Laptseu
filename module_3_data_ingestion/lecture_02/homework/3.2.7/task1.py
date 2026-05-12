SMALL_BATCH_LIMIT = 500


def calculat0e_batch(weight, price, discount = 0):
    """
    weight - вес
    price - цена
    discount - скидка, по умолчанию 0
    """

    final_sum = weight * price * (1 - discount)
    is_limit_exceeded = final_sum > SMALL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


final_sum, is_limit_exceeded = calculat0e_batch(100, 4)
print(f'Партия 1 (Морковь): Сумма {final_sum}. Превышение лимита: {is_limit_exceeded}')

final_sum, is_limit_exceeded = calculat0e_batch(50, 20, 0.1)
print(f'Партия 2 (Яблоки): Сумма {final_sum}. Превышение лимита: {is_limit_exceeded}')


